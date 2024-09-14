let cart = [];

function addcart() {
    const item = {
        name: "Women Jacket",
        price: 199.99,
        quantity: 1
    };
    cart.push(item);
    alert(`${item.name} added to cart! Price: 199.99$! Total items: ${cart.length}`);
}
