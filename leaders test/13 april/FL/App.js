import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState(() => {
    const storedCart = localStorage.getItem('cart');
    return storedCart ? JSON.parse(storedCart) : [];
  });

  useEffect(() => {
    axios.get('daica vipovo')
      .then(res => setProducts(res.data));
  }, []);

  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(cart));
  }, [cart]);

  const addToCart = (product) => {
    setCart(prev => {
      const existing = prev.find(item => item.id === product.id);
      if (existing) {
        return prev.map(item =>
          item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item
        );
      }
      return [...prev, { ...product, quantity: 1 }];
    });
  };

  const removeFromCart = (id) => {
    setCart(prev => prev.filter(item => item.id !== id));
  };

  const updateQuantity = (id, quantity) => {
    if (quantity <= 0) {
      removeFromCart(id);
    } else {
      setCart(prev =>
        prev.map(item =>
          item.id === id ? { ...item, quantity } : item
        )
      );
    }
  };

  const totalPrice = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  return (
    <div className="container">
      <h1 style={{ textAlign: 'center' }}>Products</h1>
      <div className="grid">
        {products.map(product => (
          <div key={product.id} className="card">
            <img src={product.image} alt={product.title} />
            <h4>{product.title}</h4>
            <p><strong>${product.price}</strong></p>
            <button className="button" onClick={() => addToCart(product)}>Add To Cart</button>
          </div>
        ))}
      </div>

      <h2>Cart</h2>
      <div style={{ maxWidth: '600px', margin: '0 auto' }}>
        {cart.length === 0 ? (
          <p>Cart is empty</p>
        ) : (
          <>
            {cart.map(item => (
              <div key={item.id} className="cart-item">
                <div>
                  <strong>{item.title}</strong><br />
                  ${item.price} × {item.quantity} = ${(item.price * item.quantity).toFixed(2)}
                </div>
                <div>
                  <input
                    type="number"
                    value={item.quantity}
                    min="0"
                    onChange={e => updateQuantity(item.id, parseInt(e.target.value))}
                  />
                  <button className="remove-button" onClick={() => removeFromCart(item.id)}>Remove</button>
                </div>
              </div>
            ))}
            <h3>Total: ${totalPrice.toFixed(2)}</h3>
          </>
        )}
      </div>
    </div>
  );
};

export default App;
