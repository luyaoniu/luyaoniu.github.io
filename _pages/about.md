---
permalink: /
title: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am an Assistant Teaching Professor in the Department of Electrical and Computer Engineering at the University of Washington. Before that, I was a Postdoctoral Scholar in the Network Security Lab at UW, advised by Prof. Radha Poovendran. I received my Ph.D. in 2022 under the supervision of Prof. Andrew Clark in the Department of Electrical and Computer Engineering at Worcester Polytechnic Institute, and an M.S. in Electrical and Computer Engineering from the same institution.

My research aims to develop scalable algorithms and methodologies to establish trustworthy autonomy in adversarial environments, spanning (1) safe AI, (2) verification and robust control, and (3) resilience of cyber systems. These solutions draw on artificial intelligence, optimization and control, cybersecurity, game theory, formal methods, and mechanism design, with applications in robotics, power systems, and smart transportation.

## News

{% for item in site.data.news %}
- **{{ item.date }}** — {{ item.text }}
{% endfor %}

{% if site.data.featured_publications and site.data.featured_publications.size > 0 %}
## Featured Publications

{% for pub in site.data.featured_publications %}
- {{ pub.authors }}. "{{ pub.title }}." *{{ pub.venue }}*, {{ pub.year }}.{% if pub.links %} {{ pub.links }}{% endif %}
{% endfor %}
{% endif %}

## Grants and Funding

- **PI**, UW SEED-AI Grant, 2026 — *ENGINE×LAUNCH-AI: A Multi-Agent AI System to Scale ABET-Aligned and Product-Driven Capstone Excellence Across UW Engineering and GIX*
- **co-PI**, UW ECE Curriculum Development, 2026 — *Integrating Agentic AI into EE 241: Programming, Verification, and Engineering Judgment in the Era of Coding Agents*

## Awards and Honors

- **Honorable Mention**, NeurIPS Human-AI Alignment (Bi-Align) Workshop, 2025
- **Outstanding Mentorship Award**, Department of Electrical and Computer Engineering, University of Washington, 2023
- **Certification of Reproducibility Badge**, ACM/IEEE International Conference on Cyber-Physical Systems (ICCPS), 2022
- **Best Paper Session**, ACM/IEEE International Conference on Cyber-Physical Systems (ICCPS), 2020
- **Outstanding Paper Award**, Springer Conference on Decision and Game Theory for Security (GameSec), 2018

## Professional Experience

- **Assistant Teaching Professor**, Electrical and Computer Engineering, University of Washington, 2024–present
- **Postdoctoral Scholar**, Network Security Lab, Electrical and Computer Engineering, University of Washington, 2022–2024 — Advisor: [Prof. Radha Poovendran](https://people.ece.uw.edu/radha/index.html)

## Education

- **Ph.D.**, Electrical and Computer Engineering, Worcester Polytechnic Institute, 2016–2022 — Advisor: [Prof. Andrew Clark](https://awclark587.wixsite.com/mysite)
- **M.S.**, Electrical and Computer Engineering, Worcester Polytechnic Institute, 2013–2015 — Advisor: [Prof. Kaveh Pahlavan](https://www.wpi.edu/people/faculty/kaveh)
- **B.S.E.**, Electro-Mechanical Engineering, Xidian University, Xi'an, China, 2009–2013
