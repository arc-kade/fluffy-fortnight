// Change these two values to switch currency everywhere in the app.
const LOCALE = "en-IN";
const CURRENCY = "INR";

const moneyFormatter = new Intl.NumberFormat(LOCALE, {
  style: "currency",
  currency: CURRENCY,
});

export const formatMoney = (amount) => moneyFormatter.format(amount);

// Today as YYYY-MM-DD in the user's local time (what <input type="date"> expects)
export function todayISO() {
  const now = new Date();
  const local = new Date(now.getTime() - now.getTimezoneOffset() * 60000);
  return local.toISOString().slice(0, 10);
}

export function formatDate(iso) {
  return new Date(`${iso}T00:00:00`).toLocaleDateString(LOCALE, {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}
