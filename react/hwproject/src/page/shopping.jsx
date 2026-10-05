import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../page/shopping.css";

const MOCK_SHOPPING_API_KEY = "shop_test_mock_51Hx0000000000";

// Pretend this data lives on a server
const PRODUCT_DATA = [
  { id: 1, name: "Notebook (pack of 5)", price: 8.5, emoji: "📓" },
  { id: 2, name: "Backpack", price: 34.99, emoji: "🎒" },
  { id: 3, name: "Scientific Calculator", price: 19.99, emoji: "🧮" },
  { id: 4, name: "Gel Pens (12)", price: 6.25, emoji: "🖊️" },
  { id: 5, name: "Desk Lamp", price: 22, emoji: "💡" },
  { id: 6, name: "Water Bottle", price: 11.5, emoji: "🧴" },
];

// Mock products endpoint: checks the key, then returns the catalog
function mockShoppingApi({ apiKey }) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (apiKey !== MOCK_SHOPPING_API_KEY) {
        reject(new Error("Invalid shopping API key"));
        return;
      }
      resolve(PRODUCT_DATA);
    }, 500);
  });
}

// Mock shipping endpoint: same key
function mockShippingApi({ apiKey, method, itemCount }) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (apiKey !== MOCK_SHOPPING_API_KEY) {
        reject(new Error("Invalid shopping API key"));
        return;
      }
      const rates = {
        standard: { base: 4.99, days: "5-7" },
        express: { base: 12.99, days: "1-2" },
      };
      const r = rates[method];
      resolve({
        cost: +(r.base + itemCount * 0.5).toFixed(2),
        eta: `${r.days} business days`,
      });
    }, 600);
  });
}

function Shopping() {
  const navigate = useNavigate();
  const currentUser = localStorage.getItem("currentUser");
  const cartKey = `cart:${currentUser}`;

  const [products, setProducts] = useState([]);
  const [productsLoading, setProductsLoading] = useState(true);
  const [productsError, setProductsError] = useState("");

  const [cart, setCart] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem(cartKey)) ?? [];
    } catch {
      return [];
    }
  });

  const [method, setMethod] = useState("standard");
  const [shipping, setShipping] = useState(null);
  const [shippingError, setShippingError] = useState("");
  const [shippingLoading, setShippingLoading] = useState(false);
  const [orderPlaced, setOrderPlaced] = useState(false);

  // cart holds only { id, qty }; names and prices come from the fetched products
  const cartItems = cart
    .map(i => ({ ...products.find(p => p.id === i.id), qty: i.qty }))
    .filter(i => i.name);
  const itemCount = cartItems.reduce((n, i) => n + i.qty, 0);
  const subtotal = cartItems.reduce((sum, i) => sum + i.price * i.qty, 0);
  const total = subtotal + (shipping ? shipping.cost : 0);

  // Fetch products from the mock shopping API
  useEffect(() => {
    let cancelled = false;
    mockShoppingApi({ apiKey: MOCK_SHOPPING_API_KEY })
      .then(data => { if (!cancelled) setProducts(data); })
      .catch(err => { if (!cancelled) setProductsError(err.message); })
      .finally(() => { if (!cancelled) setProductsLoading(false); });
    return () => { cancelled = true; };
  }, []);

  // Ask the mock shipping API for a rate when the cart or method changes
  useEffect(() => {
    if (itemCount === 0) {
      setShipping(null);
      return;
    }
    let cancelled = false;
    setShippingLoading(true);
    setShippingError("");

    mockShippingApi({ apiKey: MOCK_SHOPPING_API_KEY, method, itemCount })
      .then(r => { if (!cancelled) setShipping(r); })
      .catch(err => { if (!cancelled) setShippingError(err.message); })
      .finally(() => { if (!cancelled) setShippingLoading(false); });

    return () => { cancelled = true; };
  }, [itemCount, method]);

  // Save inside the handlers (not an effect) so a cart can't be overwritten by stale state
  function updateCart(next) {
    setCart(next);
    localStorage.setItem(cartKey, JSON.stringify(next));
  }

  function addToCart(id) {
    setOrderPlaced(false);
    const existing = cart.find(i => i.id === id);
    updateCart(
      existing
        ? cart.map(i => (i.id === id ? { ...i, qty: i.qty + 1 } : i))
        : [...cart, { id, qty: 1 }]
    );
  }

  function changeQty(id, delta) {
    updateCart(
      cart.map(i => (i.id === id ? { ...i, qty: i.qty + delta } : i))
          .filter(i => i.qty > 0)
    );
  }

  function removeItem(id) {
    updateCart(cart.filter(i => i.id !== id));
  }

  function placeOrder() {
    updateCart([]);
    setOrderPlaced(true);
  }

  return (
    <div className="shop-page">
      <div className="shop-header">
        <h1>Shop</h1>
        <button onClick={() => navigate("/landing")}>Back to Landing</button>
      </div>

      <div className="shop-layout">
        <div className="products">
          {productsLoading && <p>Loading products...</p>}
          {productsError && <p className="error">{productsError}</p>}

          {products.map(p => (
            <div key={p.id} className="product">
              <div className="product-emoji">{p.emoji}</div>
              <h3>{p.name}</h3>
              <p>${p.price.toFixed(2)}</p>
              <button onClick={() => addToCart(p.id)}>Add to cart</button>
            </div>
          ))}
        </div>

        <aside className="cart">
          <h2>Cart ({itemCount})</h2>

          {orderPlaced && <p className="order-ok">Order placed. Thank you!</p>}
          {productsLoading && <p>Loading cart...</p>}
          {!productsLoading && cartItems.length === 0 && !orderPlaced && (
            <p>Your cart is empty.</p>
          )}

          {cartItems.map(i => (
            <div key={i.id} className="cart-row">
              <span>{i.emoji} {i.name}</span>
              <div className="qty">
                <button onClick={() => changeQty(i.id, -1)}>-</button>
                <span>{i.qty}</span>
                <button onClick={() => changeQty(i.id, 1)}>+</button>
              </div>
              <span>${(i.price * i.qty).toFixed(2)}</span>
              <button onClick={() => removeItem(i.id)}>✕</button>
            </div>
          ))}

          {cartItems.length > 0 && (
            <>
              <label className="ship-label">
                Shipping:{" "}
                <select value={method} onChange={e => setMethod(e.target.value)}>
                  <option value="standard">Standard</option>
                  <option value="express">Express</option>
                </select>
              </label>

              <p>Subtotal: ${subtotal.toFixed(2)}</p>
              {shippingLoading && <p>Getting shipping rate...</p>}
              {shippingError && <p className="error">{shippingError}</p>}
              {shipping && !shippingLoading && (
                <p>Shipping: ${shipping.cost.toFixed(2)} ({shipping.eta})</p>
              )}
              <h3>Total: ${total.toFixed(2)}</h3>

              <button onClick={placeOrder} disabled={shippingLoading || !shipping}>
                Place order
              </button>
            </>
          )}
        </aside>
      </div>
    </div>
  );
}

export default Shopping;