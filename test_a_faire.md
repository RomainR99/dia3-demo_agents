# Tests à faire

47 tests à faire. 0 déjà faits. 47 au total.

✅ essai déjà exécuté. ☐ pas encore fait.

Aucun de ces essais ne passe sur le code actuel : comptes, flux RSS et Gmail n'y sont pas.

Emery : 19 tests. Dorian : 20 tests. Romain : 8 tests.

## Comptes et séparation

| | Qui | Test |
| --- | --- | --- |
| ☐ | Emery | Créer un compte veille technologique enregistre ses 8 flux, pas ceux de la finance. |
| ☐ | Emery | Créer un compte veille financière enregistre Investing, EasyBourse, BNP, economie.gouv.fr, FT, Cointelegraph, Cryptoast. |
| ☐ | Emery | Un deuxième compte avec le même nom est refusé. |
| ☐ | Emery | Un nom de moins de 3 caractères ou un mot de passe de moins de 4 est refusé. |
| ☐ | Emery | Un mauvais mot de passe ne connecte pas. |
| ☐ | Emery | Le même nom avec une autre casse retrouve le bon persona. |
| ☐ | Emery | L'historique du premier compte n'apparaît pas dans le second. |
| ☐ | Dorian | Dans l'interface, Quitter le bord puis ouvrir le compte B : pas d'adresse Gmail du compte A, pas de ses newsletters. |
| ☐ | Dorian | L'agent du compte B ne cite pas un objet de newsletter du compte A. |
| ☐ | Dorian | La requête SQL du ticket `jira.md` montre chaque newsletter à côté d'un seul nom de compte. |

## Flux RSS

| | Qui | Test |
| --- | --- | --- |
| ☐ | Emery | `fetch_entries` lit le flux Frandroid et sort des titres. |
| ☐ | Emery | Le rafraîchissement des 8 flux techno se termine sans erreur. |
| ☐ | Emery | Le rafraîchissement des 8 flux finance se termine sans erreur. |
| ☐ | Emery | L'extrait envoyé au modèle contient des titres et des liens de ces flux. |
| ☐ | Emery | Décocher un flux, rafraîchir : ses articles ne sont plus dans l'extrait. |
| ☐ | Emery | Un site injoignable affiche une erreur dans la barre, les autres flux restent lisibles. |
| ☐ | Emery | Après fermeture de la page, le même compte retrouve ses messages. |

## Gmail et thème

| | Qui | Test |
| --- | --- | --- |
| ☐ | Dorian | Le mois précédent d'octobre 2026 est le 1er septembre inclus, le 1er octobre exclu. |
| ☐ | Dorian | Les dates IMAP sont `01-Sep-2026` et `01-Oct-2026`. |
| ☐ | Dorian | Un e-mail HTML sans partie texte donne un sujet, une date et un résumé. |
| ☐ | Dorian | Une adresse ou un mot de passe vide est refusé avant l'appel réseau. |
| ☐ | Dorian | Un faux mot de passe d'application produit la phrase « Gmail a refusé la connexion ». |
| ☐ | Dorian | NVIDIA et « AI » passent pour la veille techno, pas pour la finance. |
| ☐ | Dorian | Une newsletter inflation et marchés passe pour la finance, pas pour la techno. |
| ☐ | Dorian | La Minute Transilien ne passe pour aucun des deux thèmes. |
| ☐ | Dorian | « Newsletter IA » passe pour la techno. |
| ☐ | Dorian | La boîte connectée du compte techno a été relue : 1 newsletter hors thème laissée de côté, 2 retenues. |
| ☐ | Dorian | La barre affiche « retenues pour : Veille technologique » et n'y met pas Transilien. |
| ☐ | Dorian | Reposer la question des newsletters : l'agent cite un objet retenu, pas un filtre Gmail inventé. |
| ☐ | Dorian | Un compte finance connecté à une autre boîte ne reçoit pas les newsletters techno. |
| ☐ | Dorian | Déconnecter Gmail efface les newsletters de ce compte et laisse les flux RSS. |

## Dialogue

| | Qui | Test |
| --- | --- | --- |
| ☐ | Emery | Une question hors veille reçoit une réponse, et l'agent dit que la veille ne contient pas le sujet. |
| ☐ | Emery | Une question sur un article RSS cite son titre et son lien. |
| ☐ | Romain | Une photo jointe part encore au modèle vision. |
| ☐ | Dorian | Une réponse vocale reste en français et cite la veille sans lire les douze articles en entier. |
| ☐ | Romain | Une clé Groq absente ou fausse s'affiche comme un message, pas comme une trace Python. |

## Cible, rien de ceci n'est codé

| | Qui | Test |
| --- | --- | --- |
| ☐ | Emery | L'agent propose des sujets techno au compte techno, et des sujets économie au compte finance. |
| ☐ | Emery | Un sujet s'appuie sur un flux RSS, une newsletter retenue, ou une tendance Twitter du thème. |
| ☐ | Emery | Twitter indisponible n'empêche pas les sujets tirés du RSS et des newsletters. |
| ☐ | Dorian | Le sujet choisi produit un texte parlable de 2 à 3 minutes. |
| ☐ | Dorian | L'utilisateur modifie le texte, et la version validée est celle qui part en vidéo. |
| ☐ | Romain | La vidéo a du son et des sous-titres alignés sur le texte validé. |
| ☐ | Romain | Sans Canva, la vidéo part quand même sur le serveur Discord du compte. |
| ☐ | Romain | Avec Canva, le message Discord contient la vidéo et le lien d'édition. |
| ☐ | Romain | Après une modification des slides, « Reprendre mon Canva » reconstruit la vidéo avec les nouvelles images, la même voix et les sous-titres. |
| ☐ | Romain | Un lien Canva collé à la main, sans identifiant de design, est refusé avec une phrase claire. |
| ☐ | Romain | Une vidéo trop lourde pour Discord part comme un lien, pas comme un fichier rejeté. |
