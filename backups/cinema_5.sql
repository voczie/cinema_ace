--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bilhetes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bilhetes (
    id integer NOT NULL,
    sessao_id integer NOT NULL,
    data_compra timestamp without time zone NOT NULL,
    valor_compra money NOT NULL
);


ALTER TABLE public.bilhetes OWNER TO postgres;

--
-- Name: bilhetes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bilhetes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.bilhetes_id_seq OWNER TO postgres;

--
-- Name: bilhetes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bilhetes_id_seq OWNED BY public.bilhetes.id;


--
-- Name: filmes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.filmes (
    id integer NOT NULL ,
    nome character varying(255) NOT NULL,
    data_estreia date NOT NULL,
    pais_origem character varying(30) NOT NULL,
    duracao interval NOT NULL,
    direcao character varying(255) NOT NULL,
    faixa_etaria character varying(10) NOT NULL
);


ALTER TABLE public.filmes OWNER TO postgres;

--
-- Name: filmes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.filmes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.filmes_id_seq OWNER TO postgres;

--
-- Name: filmes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.filmes_id_seq OWNED BY public.filmes.id;


--
-- Name: generos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.generos (
    id integer NOT NULL,
    nome character varying(255) NOT NULL
);


ALTER TABLE public.generos OWNER TO postgres;

--
-- Name: generos_filmes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.generos_filmes (
    filme_id integer NOT NULL,
    genero_id integer NOT NULL
);


ALTER TABLE public.generos_filmes OWNER TO postgres;

--
-- Name: generos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.generos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.generos_id_seq OWNER TO postgres;

--
-- Name: generos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.generos_id_seq OWNED BY public.generos.id;


--
-- Name: salas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.salas (
    id integer NOT NULL,
    numero_cadeiras integer NOT NULL,
    tamanho_tela character varying(10) NOT NULL,
    capacidade_maxima integer NOT NULL,
    tridimensional boolean NOT NULL,
    vip boolean NOT NULL
);


ALTER TABLE public.salas OWNER TO postgres;

--
-- Name: salas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.salas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.salas_id_seq OWNER TO postgres;

--
-- Name: salas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.salas_id_seq OWNED BY public.salas.id;


--
-- Name: sessoes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sessoes (
    id integer NOT NULL,
    filme_id integer NOT NULL,
    numero_sala integer NOT NULL,
    data timestamp without time zone NOT NULL,
    faixa_audio character varying(30) NOT NULL,
    legenda boolean NOT NULL
);


ALTER TABLE public.sessoes OWNER TO postgres;

--
-- Name: sessoes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sessoes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sessoes_id_seq OWNER TO postgres;

--
-- Name: sessoes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sessoes_id_seq OWNED BY public.sessoes.id;


--
-- Name: bilhetes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bilhetes ALTER COLUMN id SET DEFAULT nextval('public.bilhetes_id_seq'::regclass);


--
-- Name: filmes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.filmes ALTER COLUMN id SET DEFAULT nextval('public.filmes_id_seq'::regclass);


--
-- Name: generos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos ALTER COLUMN id SET DEFAULT nextval('public.generos_id_seq'::regclass);


--
-- Name: salas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salas ALTER COLUMN id SET DEFAULT nextval('public.salas_id_seq'::regclass);


--
-- Name: sessoes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes ALTER COLUMN id SET DEFAULT nextval('public.sessoes_id_seq'::regclass);


--
-- Data for Name: bilhetes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bilhetes (id, sessao_id, data_compra, valor_compra) FROM stdin;
1	2	2023-10-01 22:25:49.5	R$ 5,00
3	4	2023-10-29 20:33:40.593	R$ 12,00
4	10	2023-10-01 00:13:00	R$ 12,00
5	10	2023-10-01 00:14:00	R$ 16,00
6	4	2023-10-01 00:15:00	R$ 18,00
7	3	2023-10-01 00:16:00	R$ 20,00
8	2	2023-10-01 00:17:00	R$ 10,00
9	3	2023-10-01 00:18:00	R$ 25,00
10	8	2023-09-30 00:27:31.435907	R$ 18,00
11	9	2023-09-30 00:30:03.539576	R$ 30,00
12	12	2023-09-30 00:31:47.597838	R$ 30,00
\.


--
-- Data for Name: filmes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.filmes (id, nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria) FROM stdin;
1	Tudo em Todo o Lugar ao Mesmo Tempo	2022-06-23	Estados Unidos	02:19:00	Daniel Kwan, Daniel Scheinert	14
2	Como Treinar o Seu Dragao 3	2019-01-17	Estados Unidos	01:44:00	Dean DeBlois	Livre
3	Vermelho, Branco e Sangue Azul	2023-06-22	Estados Unidos	01:58:00	Matthew Lopez	16
4	Oldboy	2005-05-13	Coreia do Sul	02:00:00	Park Chan-wook	16
5	Ichi, o Assassino	2001-12-22	Japao	02:09:00	Takashi Miike	+18
6	Homem-Aranha: Atraves do Aranhaverso	2023-06-01	Estados Unidos	02:20:00	Joaquim Dos Santos, Kemp Powers, Justin K. Thompson	Livre
7	Kill Bill Vol. 1	2004-04-23	Estados Unidos	01:51:00	Quentin Tarantino	+18
8	Onde Vivem os Monstros	2010-01-15	Estados Unidos	01:41:00	Spike Jonze	10
9	Monstros S.A.	2001-11-14	Estados Unidos	01:32:00	Pete Docter	Livre
10	Universidade Monstros	2013-06-21	Estados Unidos	01:44:00	Dan Scanlon	Livre
11	Garota Exemplar	2014-10-03	Estados Unidos	02:29:00	David Fincher	14
12	O Grande Hotel Budapeste	2014-02-06	Alemanha, Estados Unidos	01:39:00	Wes Anderson	14
13	O Serviço de Entregas da Kiki	1989-07-29	Japao	01:43:00	Hayao Miyazaki	Livre
14	Psicose	1960-06-16	Estados Unidos	01:49:00	Alfred Hitchcock	14
15	Cinquenta Tons de Cinza	2015-02-11	Estados Unidos	02:08:00	Sam Taylor-Johnson	16
16	Os Oito Odiados	2015-12-25	Estados Unidos	02:48:00	Quentin Tarantino	18
17	Piratas do Caribe: No Fim do Mundo	2007-05-25	Estados Unidos	02:49:00	Gore Verbinski	12
18	A Paixão de Cristo	2004-02-25	Estados Unidos	02:07:00	Mel Gibson	14
19	Seven: Os Sete Crimes Capitais	1995-09-22	Estados Unidos	02:07:00	David Fincher	14
20	Mulan	1998-06-19	Estados Unidos	01:27:00	Tony Bancroft, Barry Cook	Livre
21	Porco Rosso: O Último Herói Romântico	1992-07-18	Japao	01:34:00	Hayao Miyazaki	Livre
22	Donnie Darko	2001-01-19	Estados Unidos	01:53:00	Richard Kelly	14
23	O Chamado vs. O Grito	2016-06-18	Japao	01:38:00	Koji Shiraishi	16
24	Você é o Próximo	2013-08-23	Estados Unidos	01:35:00	Adam Wingard	16
25	Tokyo Gore Police	2008-01-01	Japao	01:50:00	Yoshihiro Nishimura	18
26	Barbie	2023-07-21	Estados Unidos	01:54:00	Greta Gerwig	12
27	Sexta-Feira 13	1980-05-09	Estados Unidos	01:35:00	Sean S. Cunningham	18
\.


--
-- Data for Name: generos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.generos (id, nome) FROM stdin;
1	Acao
2	Comedia
3	Aventura
4	Animacao
5	Romance
6	Drama
7	Misterio
8	Policial
9	Suspense
10	Familia
\.


--
-- Data for Name: generos_filmes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.generos_filmes (filme_id, genero_id) FROM stdin;
1	1
1	2
1	3
2	1
2	4
2	3
6	1
6	3
6	4
3	2
3	5
4	1
4	6
4	7
5	1
5	8
5	6
7	1
7	8
7	9
8	3
8	6
8	10
9	4
9	3
9	2
10	4
10	3
10	2
\.


--
-- Data for Name: salas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.salas (id, numero_cadeiras, tamanho_tela, capacidade_maxima, tridimensional, vip) FROM stdin;
1	30	22:16	90	f	f
2	60	29:23	150	t	f
3	20	29:23	60	t	t
\.


--
-- Data for Name: sessoes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sessoes (id, filme_id, numero_sala, data, faixa_audio, legenda) FROM stdin;
1	5	1	2023-10-01 13:55:00	Japones	t
2	5	1	2023-10-01 22:30:00	Japones	f
3	2	3	2023-10-01 13:55:00	Portugues Brasileiro	f
4	6	3	2023-10-02 14:00:00	Ingles	t
5	9	2	2023-09-28 10:20:00	Portugues Brasileiro	f
6	1	3	2023-10-03 15:00:00	Ingles	t
7	3	2	2023-10-05 22:50:00	Ingles	t
8	4	1	2023-10-05 20:00:00	Coreano	t
9	2	2	2023-10-02 10:00:00	Portugues Dublado	f
10	7	3	2023-10-01 14:50:00	Ingles	t
11	8	3	2023-10-07 13:20:00	Ingles	f
12	9	3	2023-10-10 18:40:00	Portugues Brasileiro	f
13	10	2	2023-10-09 15:00:00	Portugues Brasileiro	f
\.


--
-- Name: bilhetes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bilhetes_id_seq', 12, true);


--
-- Name: filmes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.filmes_id_seq', 27, true);


--
-- Name: generos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.generos_id_seq', 11, true);


--
-- Name: salas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.salas_id_seq', 3, true);


--
-- Name: sessoes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sessoes_id_seq', 13, true);


--
-- Name: bilhetes bilhetes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bilhetes
    ADD CONSTRAINT bilhetes_pkey PRIMARY KEY (id);


--
-- Name: filmes filmes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.filmes
    ADD CONSTRAINT filmes_pkey PRIMARY KEY (id);


--
-- Name: generos_filmes generos_filmes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos_filmes
    ADD CONSTRAINT generos_filmes_pkey PRIMARY KEY (filme_id, genero_id);


--
-- Name: generos generos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos
    ADD CONSTRAINT generos_pkey PRIMARY KEY (id);


--
-- Name: salas salas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_pkey PRIMARY KEY (id);


--
-- Name: sessoes sessoes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes
    ADD CONSTRAINT sessoes_pkey PRIMARY KEY (id);


--
-- Name: bilhetes bilhetes_sessao_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bilhetes
    ADD CONSTRAINT bilhetes_sessao_id_fkey FOREIGN KEY (sessao_id) REFERENCES public.sessoes(id) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- Name: generos_filmes generos_filmes_filme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos_filmes
    ADD CONSTRAINT generos_filmes_filme_id_fkey FOREIGN KEY (filme_id) REFERENCES public.filmes(id) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- Name: generos_filmes generos_filmes_genero_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos_filmes
    ADD CONSTRAINT generos_filmes_genero_id_fkey FOREIGN KEY (genero_id) REFERENCES public.generos(id) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- Name: sessoes sessoes_filme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes
    ADD CONSTRAINT sessoes_filme_id_fkey FOREIGN KEY (filme_id) REFERENCES public.filmes(id) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- Name: sessoes sessoes_numero_sala_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes
    ADD CONSTRAINT sessoes_numero_sala_fkey FOREIGN KEY (numero_sala) REFERENCES public.salas(id) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- PostgreSQL database dump complete
--

