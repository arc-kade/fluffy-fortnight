# Money Manager

A React app for tracking income and expenses. Accounts and data live in the browser's localStorage.

## Run it

```
npm install
npm run dev
```

Open the address Vite prints (usually http://localhost:5173).

`npm install` pulls in: `react`, `react-dom`, `react-router-dom`, and (dev) `vite`, `@vitejs/plugin-react`.

## Structure

```
src/
  pages/        Login, Register, Landing (one file per screen)
  components/   Navbar, SummaryCards, TransactionForm, TransactionList,
                CategoryBreakdown, ProtectedRoute, PublicRoute
  utils/        storage.js (all localStorage access), format.js, categories.js
  styles/       global.css, auth.css, landing.css
  App.jsx       routes
  main.jsx      entry point
```

## How it works

- `/login` and `/register` are public. Logged-in users are redirected to `/landing`.
- `/landing` is protected. Logged-out visitors are redirected to `/login`.
- Each user's transactions are stored under `mm_transactions:<username>`, so accounts never see each other's data. Logging out keeps the data.
- Usernames are case-insensitive (`Alice` and `alice` are the same account).

## Customising

- Currency: change `LOCALE` and `CURRENCY` at the top of `src/utils/format.js`.
- Categories: edit the lists in `src/utils/categories.js`.

## Limits

Passwords are stored in plain text in localStorage and anyone with access to the browser can read them. That is fine for learning, but a real app needs a backend that hashes passwords and issues sessions.
