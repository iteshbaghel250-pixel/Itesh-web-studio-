index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Itesh Web Studio | Premium Website Developer</title>
<meta name="description" content="Itesh Web Studio - Modern websites for restaurants, gyms, shops and businesses.">
<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}
html{
    scroll-behavior:smooth;
}
body{
    font-family:Arial,Helvetica,sans-serif;
    background:#07070b;
    color:#fff;
    line-height:1.6;
}
a{
    text-decoration:none;
    color:inherit;
}
/* NAVBAR */
header{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    z-index:1000;
    background:rgba(7,7,11,.85);
    backdrop-filter:blur(15px);
    border-bottom:1px solid #24242d;
}
nav{
    max-width:1150px;
    margin:auto;
    padding:18px 25px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}
.logo{
    font-size:23px;
    font-weight:800;
}
.logo span{
    color:#00f5a0;
}
.nav-links{
    display:flex;
    gap:25px;
}
.nav-links a{
    color:#c9c9d2;
    font-size:14px;
    transition:.3s;
}
.nav-links a:hover{
    color:#00f5a0;
}
/* HERO */
.hero{
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:130px 20px 80px;
    background:
    radial-gradient(circle at 50% 20%,#12352d 0%,transparent 35%),
    #07070b;
}
.hero-content{
    max-width:900px;
}
.badge{
    display:inline-block;
    padding:8px 17px;
    border:1px solid #00f5a0;
    color:#00f5a0;
    border-radius:50px;
    font-size:13px;
    margin-bottom:22px;
}
.hero h1{
    font-size:clamp(42px,7vw,78px);
    line-height:1.05;
    margin-bottom:22px;
    font-weight:900;
}
.hero h1 span{
    color:#00f5a0;
}
.hero p{
    max-width:680px;
    margin:auto;
    color:#b8b8c3;
    font-size:18px;
}
.buttons{
    margin-top:32px;
    display:flex;
    justify-content:center;
    gap:15px;
    flex-wrap:wrap;
}
.btn{
    padding:14px 25px;
    border-radius:9px;
    font-weight:bold;
    display:inline-block;
    transition:.3s;
}
.primary{
    background:#00f5a0;
    color:#04100b;
}
.secondary{
    border:1px solid #444451;
    color:#fff;
}
.whatsapp{
    background:#20d76b;
    color:#fff;
}
.btn:hover{
    transform:translateY(-3px);
}
/* GENERAL */
section{
    padding:95px 20px;
}
.container{
    max-width:1100px;
    margin:auto;
}
.section-heading{
    text-align:center;
    margin-bottom:50px;
}
.section-heading small{
    color:#00f5a0;
    font-weight:bold;
    letter-spacing:2px;
}
.section-heading h2{
    font-size:40px;
    margin-top:8px;
}
/* ABOUT */
.about-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:35px;
    align-items:center;
}
.about-card{
    background:#111118;
    border:1px solid #262630;
    border-radius:18px;
    padding:35px;
}
.about-card h3{
    font-size:28px;
    margin-bottom:15px;
}
.about-card p{
    color:#aaaab5;
}
.skills{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:15px;
}
.skill{
    padding:20px;
    background:#111118;
    border:1px solid #262630;
    border-radius:12px;
}
.skill strong{
    display:block;
    color:#00f5a0;
    margin-bottom:5px;
}
/* SERVICES */
.services{
    background:#0b0b10;
}
.cards{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:22px;
}
.card{
    background:#12121a;
    border:1px solid #272733;
    padding:30px;
    border-radius:18px;
    transition:.3s;
}
.card:hover{
    transform:translateY(-8px);
    border-color:#00f5a0;
}
.icon{
    font-size:35px;
    margin-bottom:15px;
}
.card h3{
    margin-bottom:10px;
}
.card p{
    color:#a7a7b2;
}
/* PROJECTS */
.projects{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:22px;
}
.project{
    overflow:hidden;
    border-radius:18px;
    background:#12121a;
    border:1px solid #272733;
}
.project-top{
    height:180px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:50px;
    background:linear-gradient(135deg,#172c27,#11111a);
}
.project-info{
    padding:25px;
}
.project-info h3{
    margin-bottom:8px;
}
.project-info p{
    color:#aaaab5;
    font-size:14px;
}
.project-tag{
    display:inline-block;
    margin-top:15px;
    padding:6px 10px;
    background:#09251c;
    color:#00f5a0;
    border-radius:5px;
    font-size:12px;
}
/* PRICING */
.pricing{
    background:#0b0b10;
}
.price-card{
    max-width:500px;
    margin:auto;
    padding:40px;
    background:#12121a;
    border:1px solid #00f5a0;
    border-radius:20px;
    text-align:center;
    box-shadow:0 0 40px rgba(0,245,160,.08);
}
.price{
    font-size:48px;
    font-weight:900;
    margin:15px 0;
}
.price span{
    color:#00f5a0;
}
.price-card ul{
    list-style:none;
    text-align:left;
    margin:25px 0;
}
.price-card li{
    padding:9px 0;
    color:#c3c3cc;
}
.price-card li::before{
    content:"✓";
    color:#00f5a0;
    font-weight:bold;
    margin-right:10px;
}
/* CONTACT */
.contact-box{
    background:
    radial-gradient(circle at 50% 0%,#12352d,transparent 50%),
    #111118;
    border:1px solid #292933;
    border-radius:22px;
    padding:55px 25px;
    text-align:center;
}
.contact-box h2{
    font-size:42px;
    margin-bottom:12px;
}
.contact-box p{
    color:#aaaab5;
    margin-bottom:25px;
}
.contact-details{
    margin:25px 0;
    color:#d0d0d8;
}
.contact-details strong{
    color:#00f5a0;
}
/* FOOTER */
footer{
    padding:30px 20px;
    text-align:center;
    background:#050508;
    border-top:1px solid #20202a;
    color:#777783;
}
.footer-name{
    color:#fff;
    font-weight:bold;
}
/* MOBILE */
@media(max-width:800px){
    .nav-links{
        display:none;
    }
    .about-grid{
        grid-template-columns:1fr;
    }
    .cards,
    .projects{
        grid-template-columns:1fr;
    }
    .skills{
        grid-template-columns:1fr 1fr;
    }
    .section-heading h2{
        font-size:32px;
    }
    .contact-box h2{
        font-size:32px;
    }
}
@media(max-width:500px){
    .hero h1{
        font-size:43px;
    }
    .hero p{
        font-size:16px;
    }
    .skills{
        grid-template-columns:1fr;
    }
    .price-card{
        padding:28px 20px;
    }
}
</style>
</head>
<body>
<!-- NAVBAR -->
<header>
<nav>
<div class="logo">
Itesh <span>Web Studio</span>
</div>
<div class="nav-links">
<a href="#home">Home</a>
<a href="#about">About</a>
<a href="#services">Services</a>
<a href="#projects">Projects</a>
<a href="#pricing">Pricing</a>
<a href="#contact">Contact</a>
</div>
</nav>
</header>
<!-- HERO -->
<section class="hero" id="home">
<div class="hero-content">
<div class="badge">
🚀 Available for New Projects
</div>
<h1>
I Build <span>Premium Websites</span><br>
For Modern Businesses
</h1>
<p>
Itesh Web Studio helps restaurants, gyms, shops and local businesses
build a strong online presence with modern, responsive and professional websites.
</p>
<div class="buttons">
<a class="btn primary" href="#projects">
View My Work
</a>
<a class="btn whatsapp"
href="https://wa.me/919039853662"
target="_blank">
💬 WhatsApp Me
</a>
</div>
</div>
</section>
<!-- ABOUT -->
<section id="about">
<div class="container">
<div class="section-heading">
<small>ABOUT ME</small>
<h2>Who I Am</h2>
</div>
<div class="about-grid">
<div class="about-card">
<h3>Hi, I'm Itesh 👋</h3>
<p>
I'm a freelance website developer and the founder of
<strong>Itesh Web Studio</strong>.
I create clean, modern and mobile-friendly websites
that help businesses look professional online.
</p>
<br>
<p>
My focus is simple:
<strong>beautiful design + fast performance + easy customer contact.</strong>
</p>
</div>
<div class="skills">
<div class="skill">
<strong>HTML</strong>
Modern Website Structure
</div>
<div class="skill">
<strong>CSS</strong>
Responsive Design
</div>
<div class="skill">
<strong>JavaScript</strong>
Interactive Features
</div>
<div class="skill">
<strong>Responsive</strong>
Mobile Friendly
</div>
</div>
</div>
</div>
</section>
<!-- SERVICES -->
<section class="services" id="services">
<div class="container">
<div class="section-heading">
<small>WHAT I DO</small>
<h2>My Services</h2>
</div>
<div class="cards">
<div class="card">
<div class="icon">🍽️</div>
<h3>Restaurant Websites</h3>
<p>
Modern restaurant websites with menu, gallery,
location, contact and WhatsApp integration.
</p>
</div>
<div class="card">
<div class="icon">💪</div>
<h3>Gym Websites</h3>
<p>
Professional gym websites with services,
membership plans, trainers and enquiry options.
</p>
</div>
<div class="card">
<div class="icon">🏪</div>
<h3>Business Websites</h3>
<p>
Professional websites for shops, agencies,
startups and local businesses.
</p>
</div>
<div class="card">
<div class="icon">🎓</div>
<h3>School Websites</h3>
<p>
School websites with admission information,
gallery, notices and contact details.
</p>
</div>
<div class="card">
<div class="icon">📱</div>
<h3>Mobile Friendly</h3>
<p>
Every website is designed to work smoothly
on smartphones, tablets and computers.
</p>
</div>
<div class="card">
<div class="icon">⚡</div>
<h3>Fast & Modern</h3>
<p>
Clean layouts and modern designs focused
on a professional customer experience.
</p>
</div>
</div>
</div>
</section>
<!-- PROJECTS -->
<section id="projects">
<div class="container">
<div class="section-heading">
<small>MY WORK</small>
<h2>Featured Projects</h2>
</div>
<div class="projects">
<div class="project">
<div class="project-top">
🍽️
</div>
<div class="project-info">
<h3>Premium Restaurant</h3>
<p>
Modern restaurant website with menu,
gallery, location and WhatsApp enquiry.
</p>
<span class="project-tag">
Restaurant Website
</span>
</div>
</div>
<div class="project">
<div class="project-top">
💪
</div>
<div class="project-info">
<h3>Fitness & Gym</h3>
<p>
Professional fitness website designed
for memberships and customer enquiries.
</p>
<span class="project-tag">
Gym Website
</span>
</div>
</div>
<div class="project">
<div class="project-top">
🏢
</div>
<div class="project-info">
<h3>Business Website</h3>
<p>
Clean corporate-style website for
business branding and online presence.
</p>
<span class="project-tag">
Business Website
</span>
</div>
</div>
</div>
</div>
</section>
<!-- PRICING -->
<section class="pricing" id="pricing">
<div class="container">
<div class="section-heading">
<small>START YOUR PROJECT</small>
<h2>Website Package</h2>
</div>
<div class="price-card">
<h3>Professional Business Website</h3>
<div class="price">
₹10,000<span>+</span>
</div>
<ul>
<li>Modern Premium Design</li>
<li>Mobile Responsive Website</li>
<li>Home, About & Services</li>
<li>Gallery Section</li>
<li>WhatsApp Integration</li>
<li>Google Maps Integration</li>
<li>Contact Section</li>
<li>Basic SEO Setup</li>
<li>Free Initial Support</li>
</ul>
<a
class="btn whatsapp"
href="https://wa.me/919039853662?text=Hello%20Itesh%2C%20I%20want%20to%20discuss%20a%20website%20project."
target="_blank">
Get Your Website
</a>
</div>
</div>
</section>
<!-- CONTACT -->
<section id="contact">
<div class="container">
<div class="contact-box">
<h2>Let's Build Something Great 🚀</h2>
<p>
Have a business and need a professional website?
Let's discuss your project.
</p>
<div class="contact-details">
<p>
📱 <strong>WhatsApp:</strong>
+91 90398 53662
</p>
<p>
📍 <strong>Location:</strong>
Alirajpur, Tehsil Jobat, Gram Panchayat Khandala, Madhya Pradesh
</p>
</div>
<div class="buttons">
<a
class="btn whatsapp"
href="https://wa.me/919039853662"
target="_blank">
💬 Start WhatsApp Chat
</a>
<a
class="btn secondary"
href="tel:+919039853662">
📞 Call Me
</a>
</div>
</div>
</div>
</section>
<!-- FOOTER -->
<footer>
<p>
© 2026 <span class="footer-name">Itesh Web Studio</span>
</p>
<p>
Websites • Design • Development
</p>
</footer>
<script>
document.querySelectorAll('a[href^="#"]').forEach(function(link){
    link.addEventListener("click",function(e){
        const target=document.querySelector(
            this.getAttribute("href")
        );
        if(target){
            e.preventDefault();
            target.scrollIntoView({
                behavior:"smooth"
            });
        }
    });
});
console.log("Itesh Web Studio Portfolio Loaded 🚀");
</script>
</body>
</html>
