# 🏆 Olympic AI HCMUS 2026 — Academic Arena & Study Hub

[![Vercel Deployment](https://img.shields.io/badge/Vercel-Live-success?style=for-the-badge&logo=vercel&logoColor=white)](https://olpai26.vercel.app/hub)
[![KaTeX Rigor](https://img.shields.io/badge/KaTeX-LaTeX%20Typesetting-blue?style=for-the-badge&logo=latex&logoColor=white)](https://katex.org/)
[![Vite 5](https://img.shields.io/badge/Vite-5.4-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![React 18](https://img.shields.io/badge/React-18.3-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Curriculum](https://img.shields.io/badge/Question%20Matrix-600%20Problems-emerald?style=for-the-badge)](https://olpai26.vercel.app/hub)
[![Theme](https://img.shields.io/badge/Theme-OLED%20Pure%20Black-000000?style=for-the-badge)](https://olpai26.vercel.app/hub)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

> **Official Academic Preparation Arena & Intensive Study Hub for the Olympic AI HCMUS 2026 Competition.**  
> Engineered for world-class mathematical rigor, zero-lag single-bundle performance, pure OLED dark aesthetics, and an extensive 600-question curriculum matrix.

---

## 🌐 Live Production Deployments

| Platform | Target Route | Description |
|---|---|---|
| **Primary Academic Hub** | [olpai26.vercel.app/hub](https://olpai26.vercel.app/hub) | **Full Academic Arena & Study Hub** (Grand Lobby, Mistake Vault, LaTeX Proofs, Curated Lectures, Telemetry HUD) |
| **Alternative Hub Route** | [olpai26.vercel.app/study](https://olpai26.vercel.app/study) | Direct alias rewrite to the standalone Academic Hub bundle |
| **Interactive Exam Simulator** | [olpai26.vercel.app](https://olpai26.vercel.app) | React + Vite Interactive Quiz Runner SPA |

---

## 🏛️ Executive Architectural Overview

Olympic AI HCMUS 2026 requires mastery spanning theoretical probability, linear algebra, algorithmic Python vectorization, and deep learning architectures (Vision & NLP). The platform provides a distraction-free, professional environment modeled after top-tier academic portals and mathematical journals.

### Dual-Interface Architecture
1. **Grand Academic Lobby**:
   - **Mission Control Dashboard**: High-level telemetry displaying Questions Answered, Total Points (`PTS`), and Mastered Accuracy.
   - **Curriculum Trackers**: Live progress bars across four foundational academic pillars:
     - *Foundations & Probability*
     - *Compute & Vectorized Engineering*
     - *Deep Learning & Computer Vision*
     - *NLP & Foundation Models*
   - **Real-Time Mode Launchers**:
     - ⚡ **Sprint Training**: 30-minute rapid-fire challenge across core algorithmic concepts.
     - 📝 **Topic Mock Tests**: Complete 60-question Olympic-standard simulated examination with live timer.
     - 🛡️ **Mistake Vault Replay**: Dedicated error-collection arena that pulls directly from local flawed attempts for high-retention revision.
2. **Academic Arena & Problem Cockpit**:
   - **3-Pane Split View**:
     - *Left Pane*: Exam Selector, Question Matrix Palette with status color-coding, and Module Filters.
     - *Center Stage*: High-precision LaTeX problem statement, multi-choice option cards with instant feedback, and step-by-step mathematical proofs.
     - *Right Inspector*: 4-tier tabbed analysis suite (Theory Handbook, Mathematical Proofs, Curated Lecture Player, and Essay Rubric).

---

## ✨ Core Features & Innovations

### 📐 Pure LaTeX Mathematical Typesetting (KaTeX)
- Every mathematical expression, matrix transformation, calculus gradient, and statistical formulation is rendered via native KaTeX (`$...$` inline and `$$...$$` block display).
- Typography leverages academic serif fonts (**Computer Modern** / **STIX Two Text**), recreating the reading experience of LaTeX papers and academic olympiads.

### 🖤 Pure OLED Dark Aesthetic (`#000000`)
- Deep true-black background engineered for marathon study sessions without optical glare.
- Subtle translucent glassmorphic borders (`rgba(255, 255, 255, 0.08)`), muted slate secondary typography, and crisp emerald/rose feedback indicators.
- Ultra-thin translucent scrollbars designed to float over content without layout shift.

### 📊 600-Question Academic Matrix
Covering **6 full official/standard mock competitions** (OLP-01 through OLP-05 + Official VOAI 2025):

| Module | Subject Domain | Question Format | Weight |
|:---:|:---|:---:|:---:|
| **Module A** | Mathematics, Linear Algebra, Calculus & Probability | 12 MCQs | 24 PTS |
| **Module B** | Python Vectorization, NumPy Broadcasting & Complexity | 16 MCQs + 2 Code | 46 PTS |
| **Module C** | Machine Learning, Deep Learning, CV & Transformers | 30 MCQs | 30 PTS |
| **Essay Studio** | End-to-end System Architecture & Deep Learning Solutions | 4 Scenarios | 40 PTS (Rubric) |

### 🛡️ Mistake Vault (Ngân Hàng Câu Hỏi Làm Sai)
- Automatically tracks every incorrect response in browser `localStorage`.
- Allows students to filter exclusively for missed questions or launch dedicated **Mistake Replay** sessions to achieve 100% mastery.

### 🎥 Curated Academic Lecture Library & Smart Resolver
- Integrated video player linking 46+ verified educational resources (StatQuest, 3Blue1Brown, Standford CS231n/CS224n, MIT OpenCourseWare).
- Smart Topic Fallback Resolver ensures zero dead links; questions dynamically map to topic-specific master lectures if individual problem clips are updated.

### ⚡ Zero-Lag Standalone Single-Bundle
- In addition to the React SPA, the system compiles into `olympic_ai_study_hub.html` (2.9 MB self-contained bundle with embedded question banks and inline KaTeX runtime).
- Instantaneous switching between all 600 questions with sub-millisecond DOM updates and zero network latency.

---

## 📂 Repository Structure

```
olp-ai-hcmus26/
├── public/
│   ├── olympic_ai_study_hub.html   # Standalone 2.9MB Academic Study Hub bundle
│   ├── favicon.svg                 # Academic Olympic badge favicon
│   └── katex/                      # Local fallback KaTeX assets & webfonts
├── src/                            # React + Vite Interactive Quiz Runner SPA
│   ├── components/                 # UI Components (Arena, Inspector, Palette, ScoreCat)
│   ├── data/
│   │   ├── exams/                  # 6 Complete Exam JSONs (olp-01 to 05, voai-2025)
│   │   ├── theoryData.ts           # 5-Chapter Theoretical Handbook
│   │   └── videoData.ts            # Video mapping & topic resolvers
│   ├── styles/                     # CSS design systems (quiz, global, chatbot)
│   └── types/                      # TypeScript definitions (Exam, Question, Module)
├── docs/                           # Compilers & Academic Documentation
│   ├── generate_full_hub.py        # Python pipeline compiling JSONs into study hub
│   ├── generate_academic_hub.py    # Academic styling & template compiler
│   └── prompt-soan-tai-lieu-olp-ai.md
├── scripts/                        # Verification & Auditing Utilities
│   ├── validate.mjs                # Exam structure & schema validation
│   └── audit_quality.py            # Academic question quality auditor
├── CHAY_WEB_STUDY_HUB.bat          # 1-Click Windows Local Server launcher
├── vercel.json                     # Edge rewrites (/hub, /study) & security headers
├── package.json                    # Project metadata & npm scripts
├── vite.config.ts                  # Vite build & bundle configuration
└── README.md                       # Comprehensive repository documentation
```

---

## 🚀 Getting Started

### Prerequisites
- **Node.js** `>= 18.0.0`
- **npm** `>= 9.0.0`
- **Python** `>= 3.10` *(optional, only needed for regenerating the standalone HTML bundle)*

### 1. Clone the Repository
```bash
git clone https://github.com/lenamkhanhh/OLPAI26-Khanhdz.git
cd OLPAI26-Khanhdz
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Launch Development Server
```bash
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser.

### 4. Run Standalone Academic Hub Locally
To run the high-performance single-page Academic Hub directly:
- **Windows**: Double-click `CHAY_WEB_STUDY_HUB.bat`, or:
```bash
# Using Python built-in HTTP server:
python -m http.server 8080 --directory public
```
Then navigate to [http://localhost:8080/olympic_ai_study_hub.html](http://localhost:8080/olympic_ai_study_hub.html).

---

## 🔨 Building & Validation

### Validate Question Banks
Runs comprehensive schema and distribution checks across all 600 questions:
```bash
npm run validate
```
Checks include:
- Exactly 60 scored questions per exam ($A \times 12, B \times 18, C \times 30$).
- Balanced multiple-choice key distribution ($A/B/C/D$).
- 100% LaTeX syntax integrity.
- Unique prompt IDs with no duplicate questions across files.

### Production Build
```bash
npm run build
```
Build output is saved to `dist/`, including all compiled React chunks and the standalone `olympic_ai_study_hub.html` bundle.

### Local Preview
```bash
npm run preview
```

---

## ☁️ Deployment Guide (Vercel)

The project is preconfigured for instant zero-configuration deployment on **Vercel** via `vercel.json`:

```json
{
  "framework": "vite",
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "rewrites": [
    { "source": "/hub", "destination": "/olympic_ai_study_hub.html" },
    { "source": "/study", "destination": "/olympic_ai_study_hub.html" }
  ]
}
```

### Deploy via Vercel CLI
```bash
npx vercel --prod
```

Or connect the GitHub repository `lenamkhanhh/OLPAI26-Khanhdz` directly to Vercel for automated CI/CD deployments on every push to `main`.

---

## ⌨️ Arena Keyboard Shortcuts

| Shortcut | Action |
|:---:|:---|
| <kbd>1</kbd> / <kbd>2</kbd> / <kbd>3</kbd> / <kbd>4</kbd> | Select Choice A, B, C, or D |
| <kbd>←</kbd> / <kbd>→</kbd> | Navigate to Previous / Next Question |
| <kbd>Ctrl</kbd> + <kbd>Enter</kbd> | Submit Exam / Confirm Choices |
| <kbd>Esc</kbd> | Return to Grand Academic Lobby / Close Modals |

---

## 🏷️ GitHub Repository Metadata

When configuring your GitHub repository settings:
- **Description**: `🏆 Olympic AI HCMUS 2026 — Premier Academic Arena & Study Hub with 600-question matrix, KaTeX mathematical proofs, and OLED Dark Cockpit.`
- **Website**: `https://olpai26.vercel.app/hub`
- **Topics**: `olympic-ai`, `hcmus`, `machine-learning`, `deep-learning`, `computer-vision`, `nlp`, `katex`, `latex-math`, `study-hub`, `vite`, `react`, `vercel`

---

## 📄 License & Acknowledgments

- **License**: MIT License © 2026 lenamkhanhh.
- **Academic Sources & References**:
  - HCMUS Olympic AI Curriculum & Guidelines (2026).
  - VOAI (Vietnam Olympiad in Artificial Intelligence) 2025.
  - IOAI (International Olympiad in Artificial Intelligence) Academic Framework.
  - Educational lectures by *StatQuest (Josh Starmer)*, *3Blue1Brown (Grant Sanderson)*, *Stanford CS231n & CS224n*.
