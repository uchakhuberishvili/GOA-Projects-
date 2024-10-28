const searchButton = document.getElementById('search-button');
const cryptoInput = document.getElementById('crypto-input');
const cryptoData = document.getElementById('crypto-data');

searchButton.addEventListener('click', () => {
    const crypto = cryptoInput.value.toLowerCase();
    fetchCryptoData(crypto);
});

const fetchCryptoData = async (crypto) => {
    try {
        const response = await fetch(`https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=${crypto}`);
        
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        if (data.length === 0) {
            cryptoData.innerHTML = '<p>Cryptocurrency not found!</p>';
            return;
        }

        renderCryptoData(data[0]);
    } catch (error) {
        console.error("Error fetching crypto data:", error);
        cryptoData.innerHTML = '<p>Error fetching data. Please try again.</p>';
    }
};

const renderCryptoData = (data) => {
    cryptoData.innerHTML = `
        <h2>${data.name}</h2>
        <p>Price: $${data.current_price.toFixed(2)}</p>
        <p>Market Cap: $${data.market_cap.toLocaleString()}</p>
        <p>24h Change: ${data.price_change_percentage_24h.toFixed(2)}%</p>
    `;
};

setInterval(() => {
    const crypto = cryptoInput.value.toLowerCase();
    if (crypto) {
        fetchCryptoData(crypto);
    }
}, 10000);
