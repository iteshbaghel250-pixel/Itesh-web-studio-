<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dubai Spice | Premium Restaurant</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      scroll-behavior: smooth;
    }
    body {
      font-family: Arial, sans-serif;
      background: #0b0b0b;
      color: white;
      line-height: 1.6;
    }
    /* NAVBAR */
    nav {
      position: fixed;
      top: 0;
      width: 100%;
      z-index: 1000;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 7%;
      background: rgba(0,0,0,0.9);
      backdrop-filter: blur(10px);
    }
    .logo {
      font-size: 25px;
      font-weight: bold;
      color: #f5b942;
    }
    nav ul {
      display: flex;
      list-style: none;
      gap: 25px;
    }
    nav a {
      color: white;
      text-decoration: none;
      font-size: 15px;
    }
    nav a:hover {
      color: #f5b942;
    }
    /* HERO */
    .hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      padding: 100px 7% 60px;
      background:
        linear-gradient(rgba(0,0,0,.55), rgba(0,0,0,.8)),
        url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1800&q=85")
        center/cover;
    }
    .hero-content {
      max-width: 650px;
    }
    .hero small {
      color: #f5b942;
      font-size: 16px;
      letter-spacing: 2px;
    }
    .hero h1 {
      font-size: clamp(45px, 7vw, 82px);
      line-height: 1.05;
      margin: 18px 0;
    }
    .hero p {
      color: #ddd;
      font-size: 18px;
      margin-bottom: 30px;
    }
    .btn {
      display: inline-block;
      padding: 14px 25px;
      border-radius: 30px;
      text-decoration: none;
      font-weight: bold;
      margin-right: 10px;
      transition: .3s;
    }
    .primary {
      background: #f5b942;
      color: #111;
    }
    .secondary {
      border: 1px solid #fff;
      color: white;
    }
    .btn:hover {
      transform: translateY(-3px);
    }
    /* SECTIONS */
    section {
      padding: 90px 7%;
    }
    .section-title {
      text-align: center;
      margin-bottom: 45px;
    }
    .section-title span {
      color: #f5b942;
      text-transform: uppercase;
      letter-spacing: 2px;
      font-size: 14px;
    }
    .section-title h2 {
      font-size: 40px;
      margin-top: 8px;
    }
    /* ABOUT */
    .about {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 50px;
      align-items: center;
    }
    .about img {
      width: 100%;
      border-radius: 20px;
    }
    .about-text h2 {
      font-size: 42px;
      margin-bottom: 15px;
    }
    .about-text p {
      color: #bbb;
      margin-bottom: 20px;
    }
    /* MENU */
    .menu-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 25px;
    }
    .menu-card {
      background: #151515;
      padding: 18px;
      border-radius: 18px;
      border: 1px solid #292929;
      transition: .3s;
    }
    .menu-card:hover {
      transform: translateY(-7px);
      border-color: #f5b942;
    }
    .menu-card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 13px;
    }
    .menu-card h3 {
      margin-top: 15px;
    }
    .menu-card p {
      color: #aaa;
      font-size: 14px;
    }
    .price {
      display: block;
      color: #f5b942;
      font-size: 20px;
      font-weight: bold;
      margin-top: 10px;
    }
    /* FEATURES */
    .features {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }
    .feature {
      background: #151515;
      padding: 30px;
      text-align: center;
      border-radius: 15px;
    }
    .feature-icon {
      font-size: 35px;
      margin-bottom: 10px;
    }
    .feature p {
      color: #aaa;
      margin-top: 8px;
    }
    /* GALLERY */
    .gallery {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }
    .gallery img {
      width: 100%;
      height: 220px;
      object-fit: cover;
      border-radius: 12px;
      transition: .3s;
    }
    .gallery img:hover {
      transform: scale(1.03);
    }
    /* BOOKING */
    .booking {
      max-width: 850px;
      margin: auto;
      background: #151515;
      padding: 35px;
      border-radius: 20px;
    }
    form {
      display: grid;
      gap: 15px;
    }
    input, select, textarea {
      width: 100%;
      padding: 15px;
      border: 1px solid #333;
      background: #0d0d0d;
      color: white;
      border-radius: 10px;
      outline: none;
    }
    textarea {
      resize: vertical;
      min-height: 100px;
    }
    button {
      padding: 15px;
      border: none;
      border-radius: 30px;
      background: #f5b942;
      font-weight: bold;
      cursor: pointer;
      font-size: 16px;
    }
    /* CONTACT */
    .contact-box {
      text-align: center;
    }
    .contact-box p {
      color: #bbb;
      margin: 8px;
    }
    /* FOOTER */
    footer {
      text-align: center;
      padding: 30px;
      border-top: 1px solid #222;
      color: #888;
    }
    /* WHATSAPP */
    .whatsapp {
      position: fixed;
      right: 20px;
      bottom: 20px;
      width: 58px;
      height: 58px;
      background: #25D366;
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 28px;
      z-index: 999;
      box-shadow: 0 5px 20px rgba(0,0,0,.4);
    }
    /* MOBILE */
    @media(max-width: 800px) {
      nav {
        padding: 15px 5%;
      }
      nav ul {
        display: none;
      }
      .about {
        grid-template-columns: 1fr;
      }
      .menu-grid {
        grid-template-columns: 1fr;
      }
      .features {
        grid-template-columns: 1fr;
      }
      .gallery {
        grid-template-columns: repeat(2, 1fr);
      }
      .gallery img {
        height: 160px;
      }
      section {
        padding: 70px 5%;
      }
      .hero {
        padding-left: 5%;
        padding-right: 5%;
      }
    }
  </style>
</head>
<body>
  <!-- NAVBAR -->
  <nav>
    <div class="logo">DUBAI SPICE</div>
    <ul>
      <li><a href="#home">Home</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#menu">Menu</a></li>
      <li><a href="#gallery">Gallery</a></li>
      <li><a href="#booking">Reservation</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>
  <!-- HERO -->
  <section class="hero" id="home">
    <div class="hero-content">
      <small>WELCOME TO DUBAI SPICE</small>
      <h1>
        Taste the<br>
        Luxury.
      </h1>
      <p>
        Premium Indian & Arabian cuisine in the heart of Dubai.
        Experience authentic flavours, elegant ambience and unforgettable dining.
      </p>
      <a href="#menu" class="btn primary">
        Explore Menu
      </a>
      <a href="#booking" class="btn secondary">
        Book a Table
      </a>
    </div>
  </section>
  <!-- ABOUT -->
  <section id="about">
    <div class="section-title">
      <span>Our Story</span>
      <h2>More Than Just Food</h2>
    </div>
    <div class="about">
      <img
        src="https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=1000&q=85"
        alt="Restaurant"
      >
      <div class="about-text">
        <h2>Authentic Taste.<br>Modern Experience.</h2>
        <p>
          Dubai Spice brings together traditional Indian and Arabian
          flavours with a modern luxury dining experience.
        </p>
        <p>
          Our chefs use premium ingredients and authentic recipes
          to create dishes that guests remember.
        </p>
        <a href="#booking" class="btn primary">
          Reserve Your Table
        </a>
      </div>
    </div>
  </section>
  <!-- MENU -->
  <section id="menu">
    <div class="section-title">
      <span>Chef's Selection</span>
      <h2>Popular Menu</h2>
    </div>
    <div class="menu-grid">
      <div class="menu-card">
        <img src="https://images.unsplash.com/photo-1563379091339-03246963d29c?auto=format&fit=crop&w=800&q=80">
        <h3>Royal Chicken Biryani</h3>
        <p>Fragrant basmati rice with tender chicken and aromatic spices.</p>
        <span class="price">AED 48</span>
      </div>
      <div class="menu-card">
        <img src="https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=800&q=80">
        <h3>Butter Chicken</h3>
        <p>Rich tomato gravy, butter and traditional Indian spices.</p>
        <span class="price">AED 42</span>
      </div>
      <div class="menu-card">
        <img src="https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=800&q=80">
        <h3>Mixed Grill</h3>
        <p>Premium grilled meats served with fresh herbs and sauces.</p>
        <span class="price">AED 75</span>
      </div>
      <div class="menu-card">
        <img src="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=800&q=80">
        <h3>Fresh Garden Salad</h3>
        <p>Fresh vegetables, herbs and our signature dressing.</p>
        <span class="price">AED 28</span>
      </div>
      <div class="menu-card">
        <img src="https://images.unsplash.com/photo-1565299507177-b0ac66763828?auto=format&fit=crop&w=800&q=80">
        <h3>Signature Burger</h3>
        <p>Juicy premium beef with fresh vegetables and house sauce.</p>
        <span class="price">AED 38</span>
      </div>
      <div class="menu-card">
        <img src="https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=800&q=80">
        <h3>Royal Dessert</h3>
        <p>A delicious sweet ending to your dining experience.</p>
        <span class="price">AED 25</span>
      </div>
    </div>
  </section>
  <!-- FEATURES -->
  <section>
    <div class="section-title">
      <span>Why Choose Us</span>
      <h2>The Dubai Spice Experience</h2>
    </div>
    <div class="features">
      <div class="feature">
        <div class="feature-icon">👨‍🍳</div>
        <h3>Expert Chefs</h3>
        <p>Experienced chefs creating authentic flavours.</p>
      </div>
      <div class="feature">
        <div class="feature-icon">🥘</div>
        <h3>Fresh Ingredients</h3>
        <p>Premium and fresh ingredients every day.</p>
      </div>
      <div class="feature">
        <div class="feature-icon">✨</div>
        <h3>Luxury Ambience</h3>
        <p>A beautiful atmosphere for family and friends.</p>
      </div>
    </div>
  </section>
  <!-- GALLERY -->
  <section id="gallery">
    <div class="section-title">
      <span>Inside Dubai Spice</span>
      <h2>Our Gallery</h2>
    </div>
    <div class="gallery">
      <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80">
      <img src="https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?auto=format&fit=crop&w=800&q=80">
      <img src="https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=800&q=80">
      <img src="https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80">
    </div>
  </section>
  <!-- BOOKING -->
  <section id="booking">
    <div class="section-title">
      <span>Reservations</span>
      <h2>Book Your Table</h2>
    </div>
    <div class="booking">
      <form id="bookingForm">
        <input
          type="text"
          id="name"
          placeholder="Your Name"
          required
        >
        <input
          type="tel"
          id="phone"
          placeholder="Phone Number"
          required
        >
        <input
          type="date"
          id="date"
          required
        >
        <select id="guests" required>
          <option value="">Number of Guests</option>
          <option>1 Guest</option>
          <option>2 Guests</option>
          <option>3 Guests</option>
          <option>4 Guests</option>
          <option>5+ Guests</option>
        </select>
        <textarea
          id="message"
          placeholder="Special Request"
        ></textarea>
        <button type="submit">
          Confirm Reservation
        </button>
      </form>
    </div>
  </section>
  <!-- CONTACT -->
  <section id="contact">
    <div class="section-title">
      <span>Visit Us</span>
      <h2>Contact Dubai Spice</h2>
    </div>
    <div class="contact-box">
      <p>📍 Downtown Dubai, United Arab Emirates</p>
      <p>📞 +971 50 123 4567</p>
      <p>✉️ hello@dubaispice.com</p>
      <p>🕐 Open Daily: 11:00 AM – 12:00 AM</p>
      <br>
      <a
        href="https://www.google.com/maps/search/?api=1&query=Downtown+Dubai"
        target="_blank"
        class="btn primary"
      >
        Open Google Maps
      </a>
    </div>
  </section>
  <!-- FOOTER -->
  <footer>
    <p>
      © 2026 Dubai Spice. All Rights Reserved.
    </p>
    <p>
      Premium Restaurant Website Demo
    </p>
  </footer>
  <!-- WHATSAPP -->
  <a
    class="whatsapp"
    href="https://wa.me/971501234567?text=Hello%20Dubai%20Spice%2C%20I%20want%20to%20book%20a%20table."
    target="_blank"
    title="WhatsApp"
  >
    ☎
  </a>
  <!-- JAVASCRIPT -->
  <script>
    document.getElementById("bookingForm").addEventListener("submit", function(event) {
      event.preventDefault();
      const name = document.getElementById("name").value;
      const phone = document.getElementById("phone").value;
      const date = document.getElementById("date").value;
      const guests = document.getElementById("guests").value;
      const text =
        "Hello Dubai Spice!%0A%0A" +
        "I want to book a table.%0A" +
        "Name: " + encodeURIComponent(name) + "%0A" +
        "Phone: " + encodeURIComponent(phone) + "%0A" +
        "Date: " + encodeURIComponent(date) + "%0A" +
        "Guests: " + encodeURIComponent(guests);
      window.open(
        "https://wa.me/971501234567?text=" + text,
        "_blank"
      );
    });
  </script>
</body>
</html>