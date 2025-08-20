import React from 'react';
import { ShoppingCart, User, Search, Gamepad2 } from 'lucide-react';

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <div className="nav-brand">
          <Gamepad2 size={32} className="logo-icon" />
          <h1>GameGear Pro</h1>
        </div>
        
        <div className="search-bar">
          <input 
            type="text" 
            placeholder="Search gaming gear..." 
            className="search-input"
          />
          <Search size={20} className="search-icon" />
        </div>
        
        <nav className="nav-menu">
          <a href="/" className="nav-link">Home</a>
          <a href="/categories" className="nav-link">Categories</a>
          <a href="/deals" className="nav-link">Deals</a>
        </nav>
        
        <div className="nav-actions">
          <button className="icon-btn">
            <User size={24} />
          </button>
          <button className="icon-btn cart-btn">
            <ShoppingCart size={24} />
            <span className="cart-count">0</span>
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;
