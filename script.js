/* ================= PRELOADER ================= */

window.addEventListener("load", () => {

    const preloader =
        document.getElementById("preloader");

    setTimeout(() => {

        preloader.classList.add("hide");

    }, 700);

});


/* ================= MOBILE MENU ================= */

const menuBtn =
    document.getElementById("menuBtn");

const navMenu =
    document.getElementById("navMenu");

menuBtn.addEventListener("click", () => {

    navMenu.classList.toggle("open");

});


document.querySelectorAll("#navMenu a")
.forEach(link => {

    link.addEventListener("click", () => {

        navMenu.classList.remove("open");

    });

});


/* ================= SCROLL REVEAL ================= */

const revealElements =
    document.querySelectorAll(".reveal");

const revealObserver =
    new IntersectionObserver(

        entries => {

            entries.forEach(entry => {

                if(entry.isIntersecting){

                    entry.target.classList.add("active");

                    revealObserver.unobserve(
                        entry.target
                    );

                }

            });

        },

        {
            threshold:0.12
        }

    );


revealElements.forEach(element => {

    revealObserver.observe(element);

});


/* ================= COUNTERS ================= */

const counters =
    document.querySelectorAll(".counter");

let counterStarted = false;


function startCounters(){

    if(counterStarted) return;

    counterStarted = true;

    counters.forEach(counter => {

        const target =
            Number(counter.dataset.target);

        let current = 0;

        const increment =
            Math.max(1, Math.ceil(target / 60));

        const timer =
            setInterval(() => {

                current += increment;

                if(current >= target){

                    current = target;

                    clearInterval(timer);

                }

                counter.textContent =
                    current + (target === 100 ? "%" : "+");

            }, 25);

    });

}


const heroNumbers =
    document.querySelector(".hero-numbers");


const counterObserver =
    new IntersectionObserver(entries => {

        if(entries[0].isIntersecting){

            startCounters();

            counterObserver.disconnect();

        }

    });


counterObserver.observe(heroNumbers);


/* ================= SHOWREEL ================= */

const mainVideo =
    document.getElementById("mainVideo");

const playShowreel =
    document.getElementById("playShowreel");

const videoOverlay =
    document.getElementById("videoOverlay");


playShowreel.addEventListener("click", () => {

    mainVideo.play();

    videoOverlay.classList.add("hide");

});


mainVideo.addEventListener("play", () => {

    videoOverlay.classList.add("hide");

});


mainVideo.addEventListener("pause", () => {

    videoOverlay.classList.remove("hide");

});


/* ================= VIDEO AUTOPLAY ================= */

const videos =
    document.querySelectorAll("video");


videos.forEach(video => {

    video.addEventListener("error", () => {

        console.log(
            "Video file missing:",
            video.querySelector("source")?.src
        );

    });

});


/* ================= ACTIVE NAV ================= */

const sections =
    document.querySelectorAll("section[id]");

const navLinks =
    document.querySelectorAll("#navMenu a");


window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const top =
            section.offsetTop - 150;

        const height =
            section.offsetHeight;

        if(
            window.scrollY >= top &&
            window.scrollY < top + height
        ){

            current =
                section.getAttribute("id");

        }

    });


    navLinks.forEach(link => {

        link.classList.remove("active");

        if(
            link.getAttribute("href") ===
            "#" + current
        ){

            link.classList.add("active");

        }

    });

});


/* ================= CONTACT FORM ================= */

const contactForm =
    document.getElementById("contactForm");

const formStatus =
    document.getElementById("formStatus");


contactForm.addEventListener("submit", event => {

    event.preventDefault();


    const name =
        document.getElementById("name").value.trim();

    const phone =
        document.getElementById("phone").value.trim();

    const email =
        document.getElementById("email").value.trim();

    const projectType =
        document.getElementById("projectType").value;

    const budget =
        document.getElementById("budget").value;

    const message =
        document.getElementById("message").value.trim();


    if(!name || !phone || !message){

        formStatus.textContent =
            "Please fill the required fields.";

        return;

    }


    const whatsappMessage = `

Hello Itesh Web Studio,

I want to discuss a project.

Name: ${name}

Phone: ${phone}

Email: ${email || "Not provided"}

Project Type: ${projectType || "Not selected"}

Budget: ${budget || "Not selected"}

Project Details:
${message}

`;


    const whatsappURL =
        "https://wa.me/919039853662?text=" +
        encodeURIComponent(whatsappMessage);


    formStatus.textContent =
        "Opening WhatsApp...";


    window.open(
        whatsappURL,
        "_blank"
    );


    contactForm.reset();

});


/* ================= SMOOTH LINKS ================= */

document.querySelectorAll('a[href^="#"]')
.forEach(link => {

    link.addEventListener("click", event => {

        const id =
            link.getAttribute("href");

        if(
            id === "#" ||
            !document.querySelector(id)
        ){

            return;

        }

        event.preventDefault();

        const target =
            document.querySelector(id);

        const headerHeight = 80;

        window.scrollTo({

            top:
                target.offsetTop -
                headerHeight,

            behavior:"smooth"

        });

    });

});


/* ================= CONSOLE ================= */

console.log(
    "Itesh Web Studio — Premium Digital Experiences"
);
