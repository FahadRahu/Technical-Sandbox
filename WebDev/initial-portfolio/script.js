// Portfolio Website Script

document.addEventListener('DOMContentLoaded', function() {
    
    // Mobile Navigation Toggle
    // These constants select the hamburger menu, navigation menu, and navigation links
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Toggle mobile menu visibility on hamburger click
    // This makes it possible to open and close the mobile navigation menu
    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when a navigation link is clicked
    // This ensures the menu closes after selecting a link
    navLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Smooth Scrolling for Navigation Links
    // This makes clicking on navigation links scroll smoothly to the target section
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            // The substring method removes the '#' from the href attribute to get the target ID
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                const offsetTop = targetElement.offsetTop;

                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Add background to navbar on scroll
        if (scrollTop > 50) {
            // Change navbar background color when scrolled down and add shadow
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
        } else {
            // Revert navbar background color when at the top and remove shadow
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
        }

        lastScrollTop = scrollTop;
    });

    // Active navigation highlighting
    const sections = document.querySelectorAll('section');

    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                // Remove 'active' class from all links
                navLinks.forEach(link => {
                    link.classList.remove('active');
                });

                // Add 'active' class to the current section link
                const activeLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    });

    // Scroll animations for elements
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe timeline items, project cards, and skill categories
    const animatedElements = document.querySelectorAll('.timeline-item, .project-card, .skill-category');
    animatedElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(element);
    });

    // Typing effect for hero section
    // These constants select the hero title and subtitle elements
    const heroTitle = document.querySelector('.hero h1');
    const heroSubtitle = document.querySelector('.hero h2');

    // Add typing animation classes to hero title and subtitle
    heroTitle.style.overflow = 'hidden';
    heroTitle.style.borderRight = '3px solid white';
    heroTitle.style.whiteSpace = 'nowrap';
    heroTitle.style.animation = 'typing 3s steps(40, end), blink-caret 0.75s step-end infinite';

    // Add CSS for typing effect
    const style = document.createElement('style');
    style.textContent = `
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }

        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: white; }
        }
        
        .navlink.active {
            colorL #3498db;
            font-weight: bold;
        }
    `;
    document.head.appendChild(style);

    // Contact form functionality (placeholder for later implementation)
    const contactButtons = document.querySelectorAll('.btn-primary');
    contactButtons.forEach(button => {
        if (button.textContent.includes('Contact Me')) {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                const contactSection = document.querySelector('#contact');
                const offsetTop = contactSection.offsetTop - 70; // Adjust for fixed navbar height
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            });
        }
    });

    // Skill tags hover effect enhancement
    const skillTags = document.querySelectorAll('.skill-tag');
    skillTags.forEach(tag => {
        tag.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        tag.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Project cards click effect
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('click', function() {
            // Add a subtle click animation
            this.style.transform = 'translateY(-15px) scale(1.02)';
            setTimeout(() => {
                this.style.transform = 'translateY(-10px) scale(1)';
            }, 200);
        });
    });

    // Scroll to top functionality (hidden button that appears after scrolling down)
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.innerHTML = '↑';
    scrollToTopBtn.className = 'scroll-to-top';
    scrollToTopBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 1.2rem;
        cursor: pointer;
        opacity: 0;
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
    `;
    
    document.body.appendChild(scrollToTopBtn);

    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            scrollToTopBtn.style.opacity = '1';
            scrollToTopBtn.style.visibility = 'visible';
        } else {
            scrollToTopBtn.style.opacity = '0';
            scrollToTopBtn.style.visibility = 'hidden';
        }
    });

    // Enhanced hover effects for contact items
    const contactItems = document.querySelectorAll('.contact-item');
    contactItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'scale(1.2) rotate(5deg)';
                icon.style.transition = 'transform 0.3s ease';
            }
        });

        item.addEventListener('mouseleave', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });
    });

    // Preloader (optional - adds a nice loading effect before the site fully loads)
    const preloader = document.createElement('div');
    preloader.className = 'preloader';
    preloader.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #667eea;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        opacity: 1;
        visibility: visible;
        transition: all 0.5s ease;
    `;

    preloader.innerHTML = `
        <div style="
            color: white;
            font-size: 2rem;
            font-weight: bold;
            text-align: center;
        
        ">
            <div style="
                width: 50px;
                height: 50px;
                border: 5px solid rgba(255, 255, 255, 0.3);
                border-top: 3px solid white;
                border-radius: 50%;
                animation: spin 1s linear infinite;
                margin: 0 auto 1rem auto;
            "></div>
            Loading...
        </div>
    `;

    document.body.appendChild(preloader);

    // Add spin animation CSS
    const spinStyle = document.createElement('style');
    spinStyle.textContent = `
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(spinStyle);

    // Hide preloader when the page is fully loaded
    window.addEventListener('load', function() {
        this.setTimeout(() => {
            preloader.style.opacity = '0';
            preloader.style.visibility = 'hidden';
            setTimeout(() => {
                preloader.remove();
            }, 500);
        }, 500); // Delay to allow users to see the preloader
    });

    // Console welcome message
    console.log('%cWelcome to My Portfolio!', 'color: #3498db; font-size: 20px; font-weight: bold;');
    console.log('%cFeel free to explore my projects and skills.', 'color: #2ecc71; font-size: 16px;');
});