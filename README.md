index.html <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Itesh Web Studio | Premium Websites</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    scroll-behavior:smooth;
}

body{
    font-family:Arial, Helvetica, sans-serif;
    background:#070707;
    color:#fff;
    line-height:1.6;
}

a{
    text-decoration:none;
    color:inherit;
}

.container{
    width:90%;
    max-width:1200px;
    margin:auto;
}

/* NAVBAR */

nav{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    padding:18px 0;
    background:rgba(7,7,7,.85);
    backdrop-filter:blur(15px);
    z-index:1000;
    border-bottom:1px solid #222;
}

.navbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.logo{
    font-size:23px;
    font-weight:bold;
}

.logo span{
    color:#00ff99;
}

.nav-links{
    display:flex;
    gap:28px;
    list-style:none;
}

.nav-links a{
    color:#ddd;
    transition:.3s;
}

.nav-links a:hover{
    color:#00ff99;
}

/* HERO */

.hero{
    min-height:100vh;
    display:flex;
    align-items:center;
    padding-top:80px;
    background:
    radial-gradient(circle at 80% 30%, #123d2d 0, transparent 25%),
    radial-gradient(circle at 20% 80%, #102a22 0, transparent 25%);
}

.hero-content{
    max-width:800px;
}

.badge{
    display:inline-block;
    padding:8px 16px;
    border:1px solid #00ff99;
    border-radius:30px;
    color:#00ff99;
    margin-bottom:25px;
    font-size:14px;
}

.hero h1{
    font-size:clamp(45px,8vw,85px);
    line-height:1.05;
    margin-bottom:25px;
}

.hero h1 span{
    color:#00ff99;
}

.hero p{
    font-size:19px;
    color:#aaa;
    max-width:650px;
    margin-bottom:35px;
}

.buttons{
    display:flex;
    gap:15px;
    flex-wrap:wrap;
}

.btn{
    padding:14px 25px;
    border-radius:8px;
    font-weight:bold;
    transition:.3s;
    display:inline-block;
}

.primary{
    background:#00ff99;
    color:#000;
}

.primary:hover{
    transform:translateY(-4px);
    box-shadow:0 10px 30px #00ff9944;
}

.secondary{
    border:1px solid #444;
    color:#fff;
}

.secondary:hover{
    border-color:#00ff99;
    color:#00ff99;
}

/* SECTIONS */

section{
    padding:100px 0;
}

.section-title{
    text-align:center;
    margin-bottom:60px;
}

.section-title h2{
    font-size:42px;
    margin-bottom:10px;
}

.section-title p{
    color:#888;
}

/* SERVICES */

.services{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:22px;
}

.card{
    background:#101010;
    border:1px solid #222;
    padding:30px;
    border-radius:15px;
    transition:.3s;
}

.card:hover{
    transform:translateY(-8px);
    border-color:#00ff99;
}

.icon{
    font-size:38px;
    margin-bottom:18px;
}

.card h3{
    margin-bottom:12px;
}

.card p{
    color:#999;
}

/* PROJECTS */

.projects{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:25px;
}

.project{
    background:#101010;
    border-radius:15px;
    overflow:hidden;
    border:1px solid #222;
    transition:.3s;
}

.project:hover{
    transform:translateY(-8px);
}

.project-img{
    height:220px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:linear-gradient(135deg,#123c2c,#111);
    font-size:55px;
}

.project-content{
    padding:25px;
}

.project-content h3{
    margin-bottom:8px;
}

.project-content p{
    color:#999;
    margin-bottom:20px;
}

/* PRICING */

.pricing{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:25px;
}

.price-card{
    background:#101010;
    border:1px solid #292929;
    border-radius:18px;
    padding:35px;
    position:relative;
}

.price-card.featured{
    border:2px solid #00ff99;
    transform:scale(1.03);
}

.popular{
    position:absolute;
    top:-15px;
    right:20px;
    background:#00ff99;
    color:#000;
    padding:6px 14px;
    border-radius:20px;
    font-size:12px;
    font-weight:bold;
}

.price{
    font-size:45px;
    font-weight:bold;
    margin:15px 0;
}

.price span{
    font-size:16px;
    color:#888;
}

.features{
    list-style:none;
    margin:25px 0;
}

.features li{
    padding:8px 0;
    color:#bbb;
}

/* SKILLS */

.skills{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:15px;
}

.skill{
    padding:13px 22px;
    background:#101010;
    border:1px solid #292929;
    border-radius:30px;
    transition:.3s;
}

.skill:hover{
    border-color:#00ff99;
    color:#00ff99;
}

/* ABOUT */

.about{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:60px;
    align-items:center;
}

.about-box{
    background:#101010;
    padding:40px;
    border-radius:20px;
    border:1px solid #222;
}

.about h2{
    font-size:45px;
    margin-bottom:20px;
}

.about p{
    color:#999;
    margin-bottom:20px;
}

/* CTA */

.cta{
    text-align:center;
    background:linear-gradient(135deg,#0d2d22,#090909);
    border:1px solid #1e513e;
    border-radius:25px;
    padding:70px 25px;
}

.cta h2{
    font-size:45px;
    margin-bottom:15px;
}

.cta p{
    color:#999;
    max-width:650px;
    margin:0 auto 30px;
}

/* FOOTER */

footer{
    border-top:1px solid #222;
    padding:35px 0;
    text-align:center;
    color:#777;
}

footer span{
    color:#00ff99;
}

/* MOBILE */9039853662

@media(max-width:900px){

    .nav-links{
        display:none;
    }

    .services,
    .projects,
    .pricing{
        grid-template-columns:1fr;
    }

    .price-card.featured{
        transform:none;
    }

    .about{
        grid-template-columns:1fr;
    }

    .hero{
        text-align:center;
    }

    .hero p{
        margin-left:auto;
        margin-right:auto;
    }

    .buttons{
        justify-content:center;
    }

    section{
        padding:75px 0;
    }

    .section-title h2{
        font-size:34px;
    }
}
</style>
</head>

<body>

<!-- NAVBAR -->

<nav>
<div class="container navbar">

<div class="logo">
Itesh<span>WebStudio</span>
</div>

<ul class="nav-links">
<li><a href="#home">Home</a></li>
<li><a href="#services">Services</a></li>
<li><a href="#projects">Projects</a></li>
<li><a href="#pricing">Pricing</a></li>
<li><a href="#about">About</a></li>
</ul>

</div>
</nav>


<!-- HERO -->

<section class="hero" id="home">

<div class="container">

<div class="hero-content">

<div class="badge">
● Available for New Projects
</div>

<h1>
I Build <span>Websites</span><br>
That Grow Businesses.
</h1>

<p>
Modern, fast and mobile-friendly websites for restaurants,
gyms, schools, shops, startups and local businesses.
</p>

<div class="buttons">

<a href="#projects" class="btn primary">
View My Work
</a>

<a href="#contact" class="btn secondary">
Start a Project
</a>

</div>

</div>

</div>

</section>


<!-- SERVICES -->

<section id="services">

<div class="container">

<div class="section-title">
<h2>What I Can Build</h2>
<p>Professional digital solutions for modern businesses.</p>
</div>

<div class="services">

<div class="card">
<div class="icon">🍽️</div>
<h3>Restaurant Websites</h3>
<p>
Online menu, gallery, WhatsApp ordering,
Google Maps and reservation/contact system.
</p>
</div>

<div class="card">
<div class="icon">🏋️</div>
<h3>Gym Websites</h3>
<p>
Membership plans, trainer section,
gallery, contact and WhatsApp integration.
</p>
</div>

<div class="card">
<div class="icon">🏫</div>
<h3>School Websites</h3>
<p>
Admissions, notices, gallery, courses,
contact forms and complete school information.
</p>
</div>

<div class="card">
<div class="icon">🛍️</div>
<h3>Business Websites</h3>
<p>
Professional websites designed to turn
visitors into customers.
</p>
</div>

<div class="card">
<div class="icon">📱</div>
<h3>Web Apps</h3>
<p>
Interactive and responsive web applications
for different business requirements.
</p>
</div>

<div class="card">
<div class="icon">🚀</div>
<h3>Landing Pages</h3>
<p>
High-converting landing pages for products,
services and marketing campaigns.
</p>
</div>

</div>

</div>

</section>


<!-- PROJECTS -->

<section id="projects">

<div class="container">

<div class="section-title">
<h2>Featured Projects</h2>
<p>Some website concepts I can create for businesses.</p>
</div>

<div class="projects">

<div class="project">

<div class="project-img">
🍔
</div>

<div class="project-content">
<h3>Premium Restaurant</h3>
<p>
Modern restaurant website with menu,
gallery and online enquiry.
</p>

<a href="#" class="btn secondary">
View Demo →
</a>

</div>
</div>


<div class="project">

<div class="project-img">
💪
</div>

<div class="project-content">
<h3>Fitness Gym</h3>
<p>
Premium gym website with membership
plans and trainer section.
</p>

<a href="#" class="btn secondary">
View Demo →
</a>

</div>
</div>


<div class="project">

<div class="project-img">
🏫
</div>

<div class="project-content">
<h3>Modern School</h3>
<p>
Professional school website with admission
and contact sections.
</p>

<a href="#" class="btn secondary">
View Demo →
</a>

</div>
</div>

</div>

</div>

</section>


<!-- PRICING -->

<section id="pricing">

<div class="container">

<div class="section-title">

<h2>Simple Pricing</h2>

<p>
Choose a package according to your business needs.
</p>

</div>


<div class="pricing">


<div class="price-card">

<h3>Starter</h3>

<div class="price">
₹10K
<span>/ project</span>
</div>

<ul class="features">
<li>✓ 5 Professional Sections</li>
<li>✓ Mobile Responsive</li>
<li>✓ WhatsApp Button</li>
<li>✓ Google Maps</li>
<li>✓ Contact Form</li>
<li>✓ Basic SEO</li>
</ul>

<a href="#contact" class="btn secondary">
Get Started
</a>

</div>


<div class="price-card featured">

<div class="popular">
MOST POPULAR
</div>

<h3>Business</h3>

<div class="price">
₹20K
<span>/ project</span>
</div>

<ul class="features">
<li>✓ Premium Design</li>
<li>✓ Up to 10 Sections</li>
<li>✓ WhatsApp Integration</li>
<li>✓ Google Maps</li>
<li>✓ Gallery</li>
<li>✓ Contact / Enquiry Form</li>
<li>✓ Basic SEO</li>
<li>✓ Deployment Support</li>
</ul>

<a href="#contact" class="btn primary">
Choose Business
</a>

</div>


<div class="price-card">

<h3>Premium</h3>

<div class="price">
₹50K
<span>/ project</span>
</div>

<ul class="features">
<li>✓ Custom UI/UX</li>
<li>✓ Advanced Web App</li>
<li>✓ Admin Panel</li>
<li>✓ Database Integration</li>
<li>✓ Online Forms</li>
<li>✓ Business Automation</li>
<li>✓ Deployment</li>
<li>✓ Priority Support</li>
</ul>

<a href="#contact" class="btn secondary">
Let's Talk
</a>

</div>

</div>

</div>

</section>


<!-- SKILLS -->

<section>

<div class="container">

<div class="section-title">
<h2>My Tech Stack</h2>
<p>Technologies I use to build modern websites.</p>
</div>

<div class="skills">

<div class="skill">HTML5</div>
<div class="skill">CSS3</div>
<div class="skill">JavaScript</div>
<div class="skill">Responsive Design</div>
<div class="skill">UI/UX</div>
<div class="skill">GitHub</div>
<div class="skill">VS Code</div>
<div class="skill">Website Deployment</div>

</div>

</div>

</section>


<!-- ABOUT -->

<section id="about">

<div class="container about">

<div>

<h2>
Let's Build Something
<span style="color:#00ff99;">Great.</span>
</h2>

<p>
I help businesses create a strong online presence
with modern, responsive and professional websites.
</p>

<p>
My focus is simple: clean design, fast performance
and a website that makes the business look trustworthy.
</p>

<a href="#contact" class="btn primary">
Work With Me
</a>

</div>


<div class="about-box">

<h3>Why Choose Me?</h3>

<br>

<p>✓ Modern & Professional Design</p>
<p>✓ Mobile Friendly Websites</p>
<p>✓ Fast Loading Pages</p>
<p>✓ WhatsApp Integration</p>
<p>✓ Business-Focused Design</p>
<p>✓ Affordable Packages</p>
<p>✓ Deployment Support</p>

</div>

</div>

</section>


<!-- CTA -->

<section id="contact">

<div class="container">

<div class="cta">

<h2>
Have a Business Idea?
</h2>

<p>
Let's turn your idea into a professional website
that your customers can trust.
</p>

<div class="buttons">

<a href="https://wa.me/9039853662" class="btn primary">
💬 Chat on WhatsApp
</a>

<a href="mailto:your" class="btn secondary">
📧 Email Me Iteshbaghel250@gmail.com
</a>

</div>

</div>

</div>

</section>


<!-- FOOTER -->

<footer>

<div class="container">

<p>
© 2026 <span>Itesh Web Studio</span>.
All Rights Reserved.
</p>

<p>
Websites • Web Apps • Business Solutions
</p>

</div>

</footer>

</body>
</html>
