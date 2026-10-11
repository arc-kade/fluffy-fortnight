import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar.jsx";
import SummaryCards from "../components/SummaryCards.jsx";
import TransactionForm from "../components/TransactionForm.jsx";
import TransactionList from "../components/TransactionList.jsx";
import CategoryBreakdown from "../components/CategoryBreakdown.jsx";
import {
  getCurrentUser,
  loadTransactions,
  logoutUser,
  saveTransactions,
} from "../utils/storage.js";
import "../styles/landing.css";

function Landing() {
  const navigate = useNavigate();
  const user = getCurrentUser(); // ProtectedRoute guarantees this is set

  // Load this user's saved transactions once, when the page opens
  const [transactions, setTransactions] = useState(() =>
    loadTransactions(user.key)
  );
  const [filter, setFilter] = useState("all");

  // Save inside the handlers (not in an effect) so stale state can never
  // overwrite a user's saved data
  function update(next) {
    setTransactions(next);
    saveTransactions(user.key, next);
  }

  function addTransaction(transaction) {
    update([transaction, ...transactions]);
  }

  function deleteTransaction(id) {
    update(transactions.filter((t) => t.id !== id));
  }

  function handleLogout() {
    logoutUser();
    navigate("/login");
  }

  const income = transactions
    .filter((t) => t.type === "income")
    .reduce((sum, t) => sum + t.amount, 0);
  const expenses = transactions
    .filter((t) => t.type === "expense")
    .reduce((sum, t) => sum + t.amount, 0);

  // newest date first; entries on the same date keep most-recently-added first
  const visible = [...transactions]
    .filter((t) => filter === "all" || t.type === filter)
    .sort((a, b) => b.date.localeCompare(a.date) || b.createdAt - a.createdAt);

  return (
    <div className="landing">
      <Navbar displayName={user.displayName} onLogout={handleLogout} />

      <main className="landing-main">
        <SummaryCards income={income} expenses={expenses} />

        <div className="landing-grid">
          <TransactionForm onAdd={addTransaction} />

          <div className="landing-col">
            <TransactionList
              transactions={visible}
              filter={filter}
              onFilterChange={setFilter}
              onDelete={deleteTransaction}
            />
            <CategoryBreakdown transactions={transactions} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default Landing;
