// Main JS file for global interactions
console.log("System initialized. Monitoring for intrusions...");

/**
 * Audio FX System using Web Audio API
 * No external files required.
 */
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

const SoundFX = {
    muted: false,
    
    playTone: (freq, type, duration) => {
        if (SoundFX.muted) return;
        
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
    },

    playBeep: () => SoundFX.playTone(800, 'square', 0.1),
    playKeypress: () => SoundFX.playTone(600 + Math.random() * 200, 'sine', 0.05),
    playAccessGranted: () => {
        SoundFX.playTone(400, 'sine', 0.1);
        setTimeout(() => SoundFX.playTone(600, 'sine', 0.1), 100);
        setTimeout(() => SoundFX.playTone(1000, 'square', 0.4), 200);
    },
    playAccessDenied: () => {
        SoundFX.playTone(150, 'sawtooth', 0.3);
        setTimeout(() => SoundFX.playTone(100, 'sawtooth', 0.3), 300);
    },
    
    toggleMute: () => {
        SoundFX.muted = !SoundFX.muted;
        const btn = document.getElementById('muteBtn');
        if (btn) {
            btn.innerText = SoundFX.muted ? "[ SOUND: OFF ]" : "[ SOUND: ON ]";
            btn.style.color = SoundFX.muted ? "#666" : "";
            btn.style.borderColor = SoundFX.muted ? "#333" : "";
        }
    }
};

/**
 * Typewriter Effect
 */
function typeWriter(element, text, speed = 30) {
    element.innerHTML = "";
    let i = 0;
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            // Randomize typing speed slightly for realism
            const randomSpeed = speed + (Math.random() * 20 - 10);
            
            // Play sound every few chars
            if (i % 3 === 0) SoundFX.playKeypress();
            
            i++;
            setTimeout(type, randomSpeed);
        } else {
            element.classList.remove('typing-cursor');
        }
    }
    
    element.classList.add('typing-cursor');
    type();
}

/**
 * Scramble Text Effect (Matrix Decrypt)
 * Replaces characters randomly until the final text is revealed.
 */
function scrambleText(element, finalText, duration = 1000) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()';
    const startTime = Date.now();
    
    function update() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        let currentText = '';
        for (let i = 0; i < finalText.length; i++) {
            if (i < finalText.length * progress) {
                currentText += finalText[i];
            } else {
                currentText += chars[Math.floor(Math.random() * chars.length)];
            }
        }
        
        element.innerText = currentText;
        
        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.innerText = finalText; // Ensure final text is clean
        }
    }
    
    update();
}

/**
 * Matrix Rain Effect
 */
class MatrixRain {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.resize();
        
        this.chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*';
        this.drops = [];
        this.fontSize = 14;
        
        this.initDrops();
        window.addEventListener('resize', () => this.resize());
        
        this.animate();
    }
    
    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.initDrops();
    }
    
    initDrops() {
        const columns = this.canvas.width / this.fontSize;
        this.drops = [];
        for (let i = 0; i < columns; i++) {
            this.drops[i] = Math.random() * -100; // Start above screen randomly
        }
    }
    
    animate() {
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.ctx.fillStyle = '#0F0'; // Matrix Green
        this.ctx.font = this.fontSize + 'px monospace';
        
        for (let i = 0; i < this.drops.length; i++) {
            const text = this.chars.charAt(Math.floor(Math.random() * this.chars.length));
            this.ctx.fillText(text, i * this.fontSize, this.drops[i] * this.fontSize);
            
            if (this.drops[i] * this.fontSize > this.canvas.height && Math.random() > 0.975) {
                this.drops[i] = 0;
            }
            this.drops[i]++;
        }
        
        requestAnimationFrame(() => this.animate());
    }
}



// Initialize Global Elements
document.addEventListener('DOMContentLoaded', () => {
    // Start Matrix Rain
    new MatrixRain('matrixCanvas');
    
    // Mute Button Handler
    const muteBtn = document.getElementById('muteBtn');
    if (muteBtn) {
        muteBtn.addEventListener('click', SoundFX.toggleMute);
    }

    // Add click sounds to all buttons
    document.querySelectorAll('button, a').forEach(btn => {
        btn.addEventListener('mouseenter', () => SoundFX.playTone(2000, 'sine', 0.01));
        btn.addEventListener('click', () => {
             // Don't play beep for mute button specifically to avoid confusion, or keep it? 
             // Keep it.
             SoundFX.playBeep();
        });
    });

    // Typewriter for briefing
    const briefing = document.querySelector('.briefing p');
    if (briefing) {
        const text = briefing.innerText;
        typeWriter(briefing, text);
    }
});
