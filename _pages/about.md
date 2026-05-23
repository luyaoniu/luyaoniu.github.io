---
permalink: /
title: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am an Assistant Teaching Professor in the Department of Electrical and Computer Engineering at the University of Washington. I received my Ph.D. in 2022 under the supervision of Prof. Andrew Clark in the Department of Electrical and Computer Engineering at Worcester Polytechnic Institute, and an M.S. in Electrical and Computer Engineering from the same institution.

My research focuses on developing scalable algorithms and methodologies to establish trustworthy autonomy in adversarial environments, spanning (1) safe AI, (2) robust control and verification, and (3) resilient cyber systems. These solutions draw on machine learning, optimization and control, game theory, and formal methods, with applications in power systems, smart transportation, and robotics.

## News

{% for item in site.data.news limit:5 %}
- **{{ item.date }}** — {{ item.text }}
{% endfor %}

{% if site.data.featured_publications and site.data.featured_publications.size > 0 %}
## Featured Publications

{% for pub in site.data.featured_publications %}
- {{ pub.authors }}. "{{ pub.title }}." *{{ pub.venue }}*, {{ pub.year }}.{% if pub.links %} {{ pub.links }}{% endif %}
{% endfor %}
{% endif %}

## Awards and Honors

- **Outstanding Mentorship Award**, Department of Electrical and Computer Engineering, University of Washington, 2023
- **Certification of Reproducibility Badge**, ACM/IEEE International Conference on Cyber-Physical Systems (ICCPS 2022)
- **Best Paper Session**, ACM/IEEE International Conference on Cyber-Physical Systems (ICCPS 2020)
- **Outstanding Paper Award**, Springer Conference on Decision and Game Theory for Security (GameSec 2018)

## Records of Innovation / Patents

- Provisional Patent filed with CoMotion at the University of Washington, Seattle: *LDL: A Defense for Label-Based Membership Inference Attacks.* Arezoo Rajabi, Dinuka Sahabandu, Luyao Niu, Bhaskar Ramasubramanian, Radha Poovendran.

## Education and Training

- **Postdoctoral Scholar**, Network Security Lab, ECE, University of Washington — Advisor: [Prof. Radha Poovendran](https://people.ece.uw.edu/radha/index.html)
- **Ph.D.**, Electrical and Computer Engineering, Worcester Polytechnic Institute, 2022 — Advisor: [Prof. Andrew Clark](https://awclark587.wixsite.com/mysite)
- **M.S.**, Electrical and Computer Engineering, Worcester Polytechnic Institute, 2015 — Advisor: [Prof. Kaveh Pahlavan](https://www.wpi.edu/people/faculty/kaveh)
- **B.S.E.**, Electro-Mechanical Engineering, Xidian University, Xi'an, China, 2013
