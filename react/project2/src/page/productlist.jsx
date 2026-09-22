import Product from "../component/product";
function productList(){
    const products = [
        {id:1,name:"Toothpaste",price:2.50},
        {id:2,name:"Soap",price:6.00},
        {id:3,name:"Handwash",price:4.00},
        {id:4,name:"Deodorant",price:7.00},
        
    ]
    return(
        <div>
            {products.map(p=>(
                <Product key={p.id} name={p.name} price={p.price}/>
            ))}
        </div>
    )
}
export default productList;