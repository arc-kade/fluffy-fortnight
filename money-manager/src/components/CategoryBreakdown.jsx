import { formatMoney } from "../utils/format.js";

// Shows where the money goes: expense totals per category, biggest first
function CategoryBreakdown({ transactions }) {
  const expenses = transactions.filter((t) => t.type === "expense");
  const total = expenses.reduce((sum, t) => sum + t.amount, 0);

  const byCategory = {};
  expenses.forEach((t) => {
    byCategory[t.category] = (byCategory[t.category] || 0) + t.amount;
  });
  const rows = Object.entries(byCategory).sort((a, b) => b[1] - a[1]);

  return (
    <section className="panel">
      <h2>Spending by category</h2>

      {rows.length === 0 ? (
        <p className="empty">Add an expense to see your breakdown.</p>
      ) : (
        <ul className="breakdown">
          {rows.map(([category, amount]) => {
            const percent = total > 0 ? Math.round((amount / total) * 100) : 0;
            return (
              <li key={category}>
                <div className="breakdown-top">
                  <span>{category}</span>
                  <span>
                    {formatMoney(amount)} <small>({percent}%)</small>
                  </span>
                </div>
                <div className="bar">
                  <div className="bar-fill" style={{ width: `${percent}%` }} />
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );
}

export default CategoryBreakdown;
