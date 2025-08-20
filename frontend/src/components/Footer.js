import React from 'react';
import { Gamepad2, Mail, Phone, MapPin } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <div className="footer-brand">
              <Gamepad2 size={24} />
              <h3>GameGear Pro</h3>
            </div>
            <p>Your ultimate destination for premium gaming equipment.</p>
            <div className="contact-info">
              <div className="contact-item">
                <Mail size={16} />
                <span>support@gamegear.com</span>
              </div>
              <div className="contact-item">
                <Phone size={16} />
                <span>+1 (555) 123-4567</span>
              </div>
              <div className="contact-item">
                <MapPin size={16} />
                <span>Gaming District, Tech City</span>
              </div>
            </div>
          </div>
          
          <div className="footer-section">
            <h4>Categories</h4>
            <ul>
              <li><a href="/keyboards">Gaming Keyboards</a></li>
              <li><a href="/mice">Gaming Mice</a></li>
              <li><a href="/headsets">Gaming Headsets</a></li>
              <li><a href="/monitors">Gaming Monitors</a></li>
            </ul>
          </div>
          
          <div className="footer-section">
            <h4>Support</h4>
            <ul>
              <li><a href="/help">Help Center</a></li>
              <li><a href="/shipping">Shipping Info</a></li>
              <li><a href="/returns">Returns</a></li>
              <li><a href="/warranty">Warranty</a></li>
            </ul>
          </div>
          
          <div className="footer-section">
            <h4>Account</h4>
            <ul>
              <li><a href="/login">Sign In</a></li>
              <li><a href="/register">Create Account</a></li>
              <li><a href="/orders">Order History</a></li>
              <li><a href="/wishlist">Wishlist</a></li>
            </ul>
          </div>
        </div>
        
        <div className="footer-bottom">
          <p>&copy; 2025 GameGear Pro. All rights reserved.</p>
          <p>Built with ❤️ for gamers by gamers</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
