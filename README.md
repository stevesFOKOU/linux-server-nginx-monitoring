# Déploiement et sécurisation d'un serveur Linux

Mise en place d'un serveur Ubuntu hébergeant une application web Python, avec reverse proxy Nginx, sécurisation des accès et supervision. Le projet couvre l'administration système, la configuration réseau et la sécurité d'un serveur exposé.

## Technologies

Ubuntu Server, Nginx (reverse proxy), Gunicorn (WSGI), Python (backend), systemd (services), UFW (pare-feu), Fail2ban (protection brute-force), Netdata (supervision).

## Architecture

Le client envoie ses requêtes HTTP à Nginx, qui les transmet à Gunicorn. Gunicorn exécute l'application Python et renvoie la réponse.

## Déploiement

Installation et configuration d'Ubuntu Server. Mise en place du reverse proxy Nginx. Déploiement de l'application Python via Gunicorn. Création d'un service systemd pour assurer la persistance au redémarrage.

## Sécurisation

L'accès SSH est protégé par authentification par clé, avec désactivation du mot de passe. UFW restreint les ports aux services essentiels. Fail2ban bloque les tentatives de brute-force. L'objectif est de réduire la surface d'attaque et de contrôler les accès au serveur.

## Supervision

Netdata supervise en temps réel l'utilisation CPU, la mémoire, l'activité disque, le trafic réseau et les processus système (Nginx, Gunicorn). Le tableau de bord est accessible sur le port 19999.

## Captures

Monitoring Netdata : `docs/netdata.PNG`

Application accessible via navigateur : `docs/site.PNG`

## Limites et suites possibles

Le serveur n'est pas encore en HTTPS. Une mise en place de Let's Encrypt, une containerisation avec Docker, une centralisation des logs et un monitoring avancé avec Grafana sont les prochaines étapes envisagées.
