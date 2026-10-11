import { useState } from "react";
import { categoriesFor } from "../utils/categories.js";
import { todayISO } from "../utils/format.js";

function TransactionForm({ onAdd }) {
  const [type, setType] = useState("expense");
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState(categoriesFor("expense")[0]);
  const [description, setDescription] = useState("");
  const [date, setDate] = useState(todayISO());
  const [error, setError] = useState("");

  function changeType(nextType) {
    setType(nextType);
    // each type has its own category list, so reset to that list's first entry
    setCategory(categoriesFor(nextType)[0]);
  }

  function handleSubmit(e) {
    e.preventDefault();

    const value = Math.round(Number(amount) * 100) / 100;
    if (!Number.isFinite(value) || value <= 0) {
      setError("Enter an amount greater than 0");
      return;
    }
    if (!date) {
      setError("Pick a date");
      return;
    }

    setError("");
    onAdd({
      id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
      type,
      amount: value,
      category,
      description: description.trim(),
      date,
      createdAt: Date.now(),
    });

    // keep type, category and date so entering several items in a row is quick
    setAmount("");
    setDescription("");
  }

  return (
    <form className="panel tx-form" onSubmit={handleSubmit}>
      <h2>Add transaction</h2>

      <div className="type-toggle" role="group" aria-label="Transaction type">
        <button
          type="button"
          className={type === "expense" ? "active expense" : ""}
          aria-pressed={type === "expense"}
          onClick={() => changeType("expense")}
        >
          Expense
        </button>
        <button
          type="button"
          className={type === "income" ? "active income" : ""}
          aria-pressed={type === "income"}
          onClick={() => changeType("income")}
        >
          Income
        </button>
      </div>

      <label className="field">
        Amount
        <input
          type="number"
          inputMode="decimal"
          step="0.01"
          min="0.01"
          placeholder="0.00"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          required
        />
      </label>

      <label className="field">
        Category
        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          {categoriesFor(type).map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
      </label>

      <label className="field">
        Description (optional)
        <input
          type="text"
          placeholder="e.g. Groceries"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          maxLength={80}
        />
      </label>

      <label className="field">
        Date
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          required
        />
      </label>

      {error && <p className="form-error" role="alert">{error}</p>}

      <button type="submit" className="btn btn-primary">
        Add {type}
      </button>
    </form>
  );
}

export default TransactionForm;
