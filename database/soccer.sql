--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.2
-- Dumped by pg_dump version 9.5.2

-- Started on 2016-04-10 17:17:51

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- TOC entry 2265 (class 0 OID 16614)
-- Dependencies: 188
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 2306 (class 0 OID 0)
-- Dependencies: 187
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- TOC entry 2267 (class 0 OID 16624)
-- Dependencies: 190
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2307 (class 0 OID 0)
-- Dependencies: 189
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 2263 (class 0 OID 16606)
-- Dependencies: 186
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add country	7	add_country
20	Can change country	7	change_country
21	Can delete country	7	delete_country
22	Can add club	8	add_club
23	Can change club	8	change_club
24	Can delete club	8	delete_club
25	Can add position	9	add_position
26	Can change position	9	change_position
27	Can delete position	9	delete_position
28	Can add player	10	add_player
29	Can change player	10	change_player
30	Can delete player	10	delete_player
\.


--
-- TOC entry 2308 (class 0 OID 0)
-- Dependencies: 185
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 30, true);


--
-- TOC entry 2269 (class 0 OID 16632)
-- Dependencies: 192
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$24000$SSFEPGVRdaku$JZpJ+PmykplDGGyiGAd0bCVmY9WXRxtmrNEJz03uAkA=	2016-04-10 17:04:14.148361+07	t	admin			toanhcmus@gmail.com	t	t	2016-04-10 17:03:41.179216+07
\.


--
-- TOC entry 2271 (class 0 OID 16642)
-- Dependencies: 194
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 2309 (class 0 OID 0)
-- Dependencies: 193
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- TOC entry 2310 (class 0 OID 0)
-- Dependencies: 191
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- TOC entry 2273 (class 0 OID 16650)
-- Dependencies: 196
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2311 (class 0 OID 0)
-- Dependencies: 195
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 2275 (class 0 OID 16710)
-- Dependencies: 198
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- TOC entry 2312 (class 0 OID 0)
-- Dependencies: 197
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- TOC entry 2261 (class 0 OID 16596)
-- Dependencies: 184
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	service	country
8	service	club
9	service	position
10	service	player
\.


--
-- TOC entry 2313 (class 0 OID 0)
-- Dependencies: 183
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 10, true);


--
-- TOC entry 2259 (class 0 OID 16585)
-- Dependencies: 182
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2016-04-10 16:19:46.685101+07
2	auth	0001_initial	2016-04-10 16:19:47.449217+07
3	admin	0001_initial	2016-04-10 16:19:47.625252+07
4	admin	0002_logentry_remove_auto_add	2016-04-10 16:19:47.648252+07
5	contenttypes	0002_remove_content_type_name	2016-04-10 16:19:47.701266+07
6	auth	0002_alter_permission_name_max_length	2016-04-10 16:19:47.723268+07
7	auth	0003_alter_user_email_max_length	2016-04-10 16:19:47.743269+07
8	auth	0004_alter_user_username_opts	2016-04-10 16:19:47.763271+07
9	auth	0005_alter_user_last_login_null	2016-04-10 16:19:47.785282+07
10	auth	0006_require_contenttypes_0002	2016-04-10 16:19:47.791283+07
11	auth	0007_alter_validators_add_error_messages	2016-04-10 16:19:47.811284+07
12	sessions	0001_initial	2016-04-10 16:19:47.972812+07
13	service	0001_initial	2016-04-10 16:43:25.388127+07
\.


--
-- TOC entry 2314 (class 0 OID 0)
-- Dependencies: 181
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 13, true);


--
-- TOC entry 2276 (class 0 OID 16733)
-- Dependencies: 199
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
pbcpm9zm7ler7kof3huka031a00v0t75	M2IwN2RlZGI2OTZmZGIxMjEwYjJlOTllZGQzZDgwZmE4YzRjMjA0Nzp7Il9hdXRoX3VzZXJfaGFzaCI6ImJmNjRkZjVlYjQzYWNiYTc5Mjk2NjNjZWM2Y2Q5ZTU1NWJjN2FlMGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-04-24 17:04:14.151367+07
\.


--
-- TOC entry 2278 (class 0 OID 16746)
-- Dependencies: 201
-- Data for Name: service_club; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY service_club (id, name, country_id) FROM stdin;
\.


--
-- TOC entry 2315 (class 0 OID 0)
-- Dependencies: 200
-- Name: service_club_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('service_club_id_seq', 1, false);


--
-- TOC entry 2280 (class 0 OID 16754)
-- Dependencies: 203
-- Data for Name: service_country; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY service_country (id, name, short_name) FROM stdin;
1	Viet Nam	VN
2	English	EN
3	Unit State Amrican	USA
\.


--
-- TOC entry 2316 (class 0 OID 0)
-- Dependencies: 202
-- Name: service_country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('service_country_id_seq', 3, true);


--
-- TOC entry 2282 (class 0 OID 16762)
-- Dependencies: 205
-- Data for Name: service_player; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY service_player (id, name, club_id, position_id) FROM stdin;
\.


--
-- TOC entry 2317 (class 0 OID 0)
-- Dependencies: 204
-- Name: service_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('service_player_id_seq', 1, false);


--
-- TOC entry 2284 (class 0 OID 16770)
-- Dependencies: 207
-- Data for Name: service_position; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY service_position (id, short_name, description) FROM stdin;
\.


--
-- TOC entry 2318 (class 0 OID 0)
-- Dependencies: 206
-- Name: service_position_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('service_position_id_seq', 1, false);


-- Completed on 2016-04-10 17:17:51

--
-- PostgreSQL database dump complete
--

