function Navbar({ displayName, onLogout }) {
  return (
    <header className="navbar">
      <span className="navbar-brand">💰 Money Manager</span>
      <div className="navbar-right">
        <span className="navbar-user">Hi, {displayName}</span>
        <button type="button" className="btn btn-ghost" onClick={onLogout}>
          Log out
        </button>
      </div>
    </header>
  );
}

export default Navbar;
