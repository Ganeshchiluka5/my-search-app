from flask import Flask, render_template_string, request

app = Flask(__name__)

# Clean products list (no line breaks in URLs)
products = [
    {"id": 1, "name": "Gaming Laptop", "category": "Electronics", "price": 85000, "image": "https://placehold.co/300x200/4A90E2/white?text=Laptop"},
    {"id": 2, "name": "Cotton T-Shirt", "category": "Clothing", "price": 499, "image": "https://placehold.co/300x200/E74C3C/white?text=T-Shirt"},
    {"id": 3, "name": "Python Programming", "category": "Education", "price": 599, "image": "https://placehold.co/300x200/2ECC71/white?text=Book"},
    {"id": 4, "name": "Wireless Headphones", "category": "Electronics", "price": 2999, "image": "https://placehold.co/300x200/9B59B6/white?text=Headphones"},
    {"id": 5, "name": "Slim Fit Jeans", "category": "Clothing", "price": 1299, "image": "https://placehold.co/300x200/F39C12/white?text=Jeans"},
    {"id": 6, "name": "Data Science Guide", "category": "Education", "price": 799, "image": "https://placehold.co/300x200/1ABC9C/white?text=Book"}
]

HOME_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🛒 Shoppest G Wagon - Smart Search</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; }
        header { text-align: center; margin-bottom: 30px; padding: 20px; }
        h1 { color: #2c3e50; font-size: 2.5rem; margin-bottom: 10px; }
        .subtitle { color: #7f8c8d; font-size: 1.1rem; }
        .search-box { display: flex; gap: 10px; margin: 20px auto 30px; max-width: 600px; }
        input[type="text"] { flex: 1; padding: 15px; font-size: 16px; border: 2px solid #3498db; border-radius: 50px; outline: none; box-shadow: 0 2px 5px rgba(0,0,0,0.1); padding-left: 20px; }
        button { padding: 15px 30px; background: #3498db; color: white; border: none; border-radius: 50px; cursor: pointer; font-size: 16px; font-weight: bold; box-shadow: 0 4px 8px rgba(52, 152, 219, 0.3); transition: all 0.3s ease; }
        button:hover { background: #2980b9; transform: translateY(-2px); box-shadow: 0 6px 12px rgba(52, 152, 219, 0.4); }
        .results { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
        .product-card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; }
        .product-card:hover { transform: translateY(-10px); box-shadow: 0 12px 20px rgba(0,0,0,0.15); }
        .product-image { width: 100%; height: 200px; object-fit: cover; }
        .product-info { padding: 20px; }
        .product-name { font-size: 1.3rem; font-weight: bold; color: #2c3e50; margin-bottom: 8px; }
        .product-category { color: #3498db; font-size: 0.95rem; margin-bottom: 12px; }
        .product-price { font-size: 1.5rem; color: #27ae60; font-weight: bold; margin: 10px 0; }
        .btn-add { width: 100%; padding: 12px; background: #2ecc71; color: white; border: none; border-radius: 8px; font-size: 1rem; font-weight: bold; cursor: pointer; transition: background 0.3s; display: flex; align-items: center; justify-content: center; gap: 8px; }
        .btn-add:hover { background: #27ae60; }
        .no-results { text-align: center; color: #e74c3c; font-size: 1.4rem; padding: 40px; grid-column: 1 / -1; }
        @media (max-width: 600px) { .search-box { flex-direction: column; } h1 { font-size: 2rem; } }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><i class="fas fa-search"></i> ShopFast Search</h1>
            <p class="subtitle">Find products in seconds!</p>
        </header>
        <div class="search-box">
            <input type="text" id="query" placeholder="Search for products or categories..." value="{{ query }}">
            <button onclick="search()"><i class="fas fa-search"></i> Search</button>
        </div>
        <div class="results">
            {% if results %}
                {% for product in results %}
                <div class="product-card">
                    <img src="{{ product.image }}" alt="{{ product.name }}" class="product-image">
                    <div class="product-info">
                        <div class="product-name">{{ product.name }}</div>
                        <div class="product-category"><i class="fas fa-tag"></i> {{ product.category }}</div>
                        <div class="product-price">₹{{ product.price }}</div>
                        <button class="btn-add" onclick="addToCart('{{ product.name }}')">
                            <i class="fas fa-cart-plus"></i> Add to Cart
                        </button>
                    </div>
                </div>
                {% endfor %}
            {% elif query != None and query != "" %}
                <div class="no-results">
                    <i class="fas fa-exclamation-circle"></i><br>
                    No products found for "<strong>{{ query }}</strong>"
                </div>
            {% endif %}
        </div>
    </div>

    <script>
        function search() {
            const q = document.getElementById('query').value.trim();
            if (q) window.location.href = '/search?q=' + encodeURIComponent(q);
        }
        document.getElementById('query').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') search();
        });
        function addToCart(productName) {
            alert('✅ "' + productName + '" added to your cart!');
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HOME_PAGE, query="", results=[])

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        results = [p for p in products if query.lower() in p['name'].lower() or query.lower() in p['category'].lower()]
    else:
        results = []
    return render_template_string(HOME_PAGE, query=query, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
