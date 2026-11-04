## Hi there 👋
<div align="center">

<img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Playing_T-Rex_Runner.gif"
     width="50%"
     style="border-radius: 100%;"
     alt="T-Rex Runner Animation">

</div>

![JavaScript](https://img.shields.io/badge/JavaScript-32363F?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![React](https://img.shields.io/badge/React-32363F?style=for-the-badge&logo=react&logoColor=61DAFB)
![Node.js](https://img.shields.io/badge/Node.js-32363F?style=for-the-badge&logo=nodedotjs&logoColor=6DA55F)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600&display=swap');

/* MAIN BOX */
.specialization-box {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 50%;
    box-sizing: border-box;
    padding: 24px 15px;

    background:
        linear-gradient(
            110deg,
            rgba(255, 80, 150, 0.15),
            rgba(130, 80, 255, 0.18),
            rgba(40, 180, 255, 0.15)
        ),
        linear-gradient(135deg, #17151f, #29202e);

    border: 1px solid rgba(190, 120, 255, 0.4);
    border-radius: 14px;

    box-shadow:
        0 0 15px rgba(190, 80, 220, 0.18),
        0 8px 30px rgba(0, 0, 0, 0.3),
        inset 0 0 25px rgba(150, 80, 255, 0.08);

    transition: 0.35s ease;
}

.specialization-box:hover {
    transform: translateY(-4px);
    border-color: #c084fc;

    box-shadow:
        0 0 18px rgba(190, 80, 255, 0.35),
        0 0 35px rgba(70, 150, 255, 0.2),
        0 12px 35px rgba(0, 0, 0, 0.3);
}

/* TEXT */
.specialization {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;

    font-family: 'Orbitron', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 10px;
}

/* LETTER ANIMATION */
.specialization span:not(.space) {
    display: inline-block;
    opacity: 0;

    animation: letterAppear 0.5s ease forwards;

    text-shadow: 0 0 12px currentColor;
}

.specialization .space {
    width: 8px;
}

/* WEB */
.specialization span:nth-child(1) {
    color: black;
    animation-delay: 0s;
}

.specialization span:nth-child(2) {
    color: black;
    animation-delay: 1s;
}

.specialization span:nth-child(3) {
    color: black;
    animation-delay: 2s;
}


.specialization span:nth-child(5) {
    color: #f90081;
    animation-delay: 3s;
}


.specialization span:nth-child(7) {
    color: wheat;
    animation-delay: 4s;
}

.specialization span:nth-child(8) {
    color: wheat;
    animation-delay: 5s;
}

.specialization span:nth-child(9) {
    color: wheat;
    animation-delay: 6s;
}

.specialization span:nth-child(10) {
    color: wheat;
    animation-delay: 7s;
}

.specialization span:nth-child(11) {
    color: wheat;
    animation-delay: 8s;
}

.specialization span:nth-child(12) {
    color: wheat;
    animation-delay: 9s;
}

.specialization span:nth-child(13) {
    color: wheat;
    animation-delay: 10s;
}

/* DEVELOPMENT */
.specialization span:nth-child(15) {
    color: #38bdf8;
    animation-delay: 11s;
}

.specialization span:nth-child(16) {
    color: #38bdf8;
    animation-delay: 12s;
}

.specialization span:nth-child(17) {
    color: #38bdf8;
    animation-delay: 13s;
}

.specialization span:nth-child(18) {
    color: #38bdf8;
    animation-delay: 14s;
}

.specialization span:nth-child(19) {
    color: #38bdf8;
    animation-delay: 15s;
}

.specialization span:nth-child(20) {
    color: #38bdf8;
    animation-delay: 16s;
}

.specialization span:nth-child(21) {
    color: #38bdf8;
    animation-delay: 17s;
}

.specialization span:nth-child(22) {
    color: #38bdf8;
    animation-delay: 18s;
}

.specialization span:nth-child(23) {
    color: #38bdf8;
    animation-delay: 19s;
}

.specialization span:nth-child(24) {
    color: #38bdf8;
    animation-delay: 20s;
}

.specialization span:nth-child(25) {
    color: #38bdf8;
    animation-delay: 21s;
}

/* ANIMATION */
@keyframes letterAppear {
    from {
        opacity: 0;
        transform: translateY(12px);
        filter: blur(5px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}

/* .specialization span:nth-child(1)  { animation-delay: 0s; }
.specialization span:nth-child(2)  { animation-delay: 0.5s; }
.specialization span:nth-child(3)  { animation-delay: 1s; }
.specialization span:nth-child(5)  { animation-delay: 1.5s; }
.specialization span:nth-child(7)  { animation-delay: 2s; }
.specialization span:nth-child(8)  { animation-delay: 2.5s; }
.specialization span:nth-child(9)  { animation-delay: 3s; }
.specialization span:nth-child(10) { animation-delay: 3.5s; }
.specialization span:nth-child(11) { animation-delay: 4s; }
.specialization span:nth-child(12) { animation-delay: 4.5s; }
.specialization span:nth-child(13) { animation-delay: 5s; }
.specialization span:nth-child(15) { animation-delay: 5.5s; }
.specialization span:nth-child(16) { animation-delay: 6s; }
.specialization span:nth-child(17) { animation-delay: 6.5s; }
.specialization span:nth-child(18) { animation-delay: 7s; }
.specialization span:nth-child(19) { animation-delay: 7.5s; }
.specialization span:nth-child(20) { animation-delay: 8s; }
.specialization span:nth-child(21) { animation-delay: 8.5s; }
.specialization span:nth-child(22) { animation-delay: 9s; }
.specialization span:nth-child(23) { animation-delay: 9.5s; }
.specialization span:nth-child(24) { animation-delay: 10s; }
.specialization span:nth-child(25) { animation-delay: 10.5s; } */
