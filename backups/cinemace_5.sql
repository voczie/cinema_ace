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

--
-- Name: update_qnt_bilhetes_disponivel(); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.update_qnt_bilhetes_disponivel()
    LANGUAGE sql
    AS $_$create or replace procedure update_qnt_bilhetes_disponivel(
	"sessao_id" int)
language plpgsql
as $$
begin
	update sessoes
	set qnt_bilhetes_disponivel = qnt_bilhetes_disponivel - 1
	where id = sessao_id;
	
	commit;
end;$$;$_$;


ALTER PROCEDURE public.update_qnt_bilhetes_disponivel() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: filmes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.filmes (
    id integer NOT NULL,
    nome character varying(255) NOT NULL,
    data_estreia date NOT NULL,
    pais_origem character varying(30) NOT NULL,
    duracao interval NOT NULL,
    direcao character varying(255) NOT NULL,
    faixa_etaria character varying(10) NOT NULL,
    gravado_mari boolean NOT NULL
);


ALTER TABLE public.filmes OWNER TO postgres;

--
-- Name: salas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.salas (
    numero_sala integer NOT NULL,
    numero_cadeiras integer NOT NULL,
    tamanho_tela character varying(10) NOT NULL,
    capacidade_maxima integer NOT NULL,
    tridimensional boolean NOT NULL,
    vip boolean NOT NULL
);


ALTER TABLE public.salas OWNER TO postgres;

--
-- Name: sessoes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sessoes (
    id integer NOT NULL,
    filme_id integer NOT NULL,
    numero_sala integer NOT NULL,
    data timestamp without time zone NOT NULL,
    faixa_audio character varying(30) NOT NULL,
    legenda boolean NOT NULL,
    qnt_bilhetes_disponivel integer NOT NULL,
    preco_inteira money NOT NULL
);


ALTER TABLE public.sessoes OWNER TO postgres;

--
-- Name: all_sessoes; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.all_sessoes AS
 SELECT se.id,
    fi.nome,
    se.data,
    sa.numero_sala,
    se.faixa_audio,
    se.legenda,
    fi.faixa_etaria,
    sa.tridimensional,
    sa.vip,
    se.qnt_bilhetes_disponivel,
    se.preco_inteira
   FROM ((public.sessoes se
     JOIN public.filmes fi ON ((fi.id = se.filme_id)))
     JOIN public.salas sa ON ((sa.numero_sala = se.numero_sala)))
  ORDER BY se.data;


ALTER VIEW public.all_sessoes OWNER TO postgres;

--
-- Name: bilhetes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bilhetes (
    id integer NOT NULL,
    sessao_id integer NOT NULL,
    funcionario_vendedor_id character varying(11) NOT NULL,
    cliente_id character varying(11) NOT NULL,
    compra_concluida boolean NOT NULL,
    data_compra timestamp without time zone NOT NULL,
    preco_pago money NOT NULL,
    tipo_pagamento character varying(25) NOT NULL
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
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    cpf character varying(11) NOT NULL,
    flamenguista boolean NOT NULL,
    assiste_onepiece boolean NOT NULL,
    sousense boolean NOT NULL
);


ALTER TABLE public.clientes OWNER TO postgres;

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
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionarios (
    cpf character varying(11) NOT NULL,
    salario money NOT NULL
);


ALTER TABLE public.funcionarios OWNER TO postgres;

--
-- Name: generos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.generos (
    nome character varying(255) NOT NULL
);


ALTER TABLE public.generos OWNER TO postgres;

--
-- Name: generos_filmes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.generos_filmes (
    filme_id integer NOT NULL,
    genero character varying(255) NOT NULL
);


ALTER TABLE public.generos_filmes OWNER TO postgres;

--
-- Name: pessoas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pessoas (
    cpf character varying(11) NOT NULL,
    nome character varying(255) NOT NULL,
    idade integer NOT NULL,
    login character varying(60) NOT NULL,
    senha character varying(60) NOT NULL
);


ALTER TABLE public.pessoas OWNER TO postgres;

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

ALTER SEQUENCE public.salas_id_seq OWNED BY public.salas.numero_sala;


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
-- Name: salas numero_sala; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salas ALTER COLUMN numero_sala SET DEFAULT nextval('public.salas_id_seq'::regclass);


--
-- Name: sessoes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes ALTER COLUMN id SET DEFAULT nextval('public.sessoes_id_seq'::regclass);


--
-- Data for Name: bilhetes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bilhetes (id, sessao_id, funcionario_vendedor_id, cliente_id, compra_concluida, data_compra, preco_pago, tipo_pagamento) FROM stdin;
2	1	70211808458	70083172475	f	2023-11-04 09:06:46.783076	R$ 20,16	Berries
48	2	70211808458	08899698414	t	2023-11-06 22:28:05.287479	R$ 31,50	Pix
49	5	70211808458	11649047444	t	2023-11-06 22:28:31.592411	R$ 12,00	Boleto
51	1	70211808458	11649047444	t	2023-11-06 22:30:34.915156	R$ 22,40	Berries
52	3	71375850431	70083172475	t	2023-11-06 22:31:26.453	R$ 22,50	Pix
53	4	71375850431	01251843018	t	2023-11-06 22:31:55.381337	R$ 22,50	Berries
54	5	11705165486	11649047444	t	2023-11-06 22:32:30.726209	R$ 12,00	Cartao
\.


--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (cpf, flamenguista, assiste_onepiece, sousense) FROM stdin;
08899698414	t	t	f
11649047444	f	f	f
01251843018	f	t	f
70083172475	t	t	f
\.


--
-- Data for Name: filmes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.filmes (id, nome, data_estreia, pais_origem, duracao, direcao, faixa_etaria, gravado_mari) FROM stdin;
1	Oldboy	2005-05-13	Coreia do Sul	02:00:00	Park Chan-wook	16	t
2	Psicose	1960-06-16	Estados Unidos	01:49:00	Alfred Hitchcock	14	f
3	Ichi, o Assassino	2001-02-22	Japao	02:09:00	Takashi Miike	+18	t
4	Monstros S.A.	2001-11-14	Estados Unidos	01:32:00	Peter Docter	Livre	f
5	O Serviço de Entregas da Kiki	1989-07-29	Japao	01:43:00	Hayao Miyazaki	Livre	f
6	Universidade Monstros	2013-06-21	Estados Unidos	01:44:00	Dan Scanlon	Livre	t
7	Kill Bill Vol. 1	2004-04-23	Estados Unidos	01:51:00	Quentin Tarantino	+18	t
\.


--
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.funcionarios (cpf, salario) FROM stdin;
70211808458	R$ 3.000,00
11705165486	R$ 2.000,00
71375850431	R$ 5.000,00
05952777738	R$ 5.000,00
\.


--
-- Data for Name: generos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.generos (nome) FROM stdin;
Acao
Comedia
Aventura
Animacao
Romance
Drama
Misterio
Policial
Suspense
Familia
\.


--
-- Data for Name: generos_filmes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.generos_filmes (filme_id, genero) FROM stdin;
1	Acao
1	Drama
1	Misterio
7	Acao
7	Policial
7	Suspense
4	Animacao
4	Aventura
4	Comedia
6	Animacao
6	Aventura
6	Comedia
3	Acao
3	Policial
3	Drama
\.


--
-- Data for Name: pessoas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pessoas (cpf, nome, idade, login, senha) FROM stdin;
70211808458	Victoria Grisi	22	voczie	amobancodedados
08899698414	Jonas Crossfit	21	reidoshape	soulindo
11649047444	Joquinha	21	futuro_medico	quedeusmetenha
01251843018	Lemos	22	lemos	:MHS,Tb_=y66-2Pe\\}yrU1}uy
11705165486	Manel	20	mamel	paodequeijoebom
70083172475	Isaac do Vine	21	isaas	357isaquinho
71375850431	Jao	21	joaovnsousa	mozovo69
05952777738	Tales Nobre	23	genevoxy	voupassaremapa
\.


--
-- Data for Name: salas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.salas (numero_sala, numero_cadeiras, tamanho_tela, capacidade_maxima, tridimensional, vip) FROM stdin;
1	30	22:16	90	f	f
2	60	29:23	150	t	f
3	20	29:23	60	t	t
\.


--
-- Data for Name: sessoes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sessoes (id, filme_id, numero_sala, data, faixa_audio, legenda, qnt_bilhetes_disponivel, preco_inteira) FROM stdin;
2	1	2	2023-11-04 04:30:00	Coreano	t	149	R$ 35,00
3	4	2	2023-11-06 14:00:00	Português Brasileiro	f	149	R$ 25,00
4	5	3	2023-11-05 12:50:00	Japones	t	59	R$ 25,00
5	5	2	2023-11-02 22:45:37	Japones	t	148	R$ 12,00
1	3	2	2024-09-11 20:00:00	Japones	t	4	R$ 22,40
\.


--
-- Name: bilhetes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bilhetes_id_seq', 54, true);


--
-- Name: filmes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.filmes_id_seq', 7, true);


--
-- Name: salas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.salas_id_seq', 3, true);


--
-- Name: sessoes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sessoes_id_seq', 5, true);


--
-- Name: bilhetes bilhetes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bilhetes
    ADD CONSTRAINT bilhetes_pkey PRIMARY KEY (id);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (cpf);


--
-- Name: filmes filmes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.filmes
    ADD CONSTRAINT filmes_pkey PRIMARY KEY (id);


--
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (cpf);


--
-- Name: generos_filmes generos_filmes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos_filmes
    ADD CONSTRAINT generos_filmes_pkey PRIMARY KEY (filme_id, genero);


--
-- Name: generos generos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos
    ADD CONSTRAINT generos_pkey PRIMARY KEY (nome);


--
-- Name: pessoas pessoas_login_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pessoas
    ADD CONSTRAINT pessoas_login_key UNIQUE (login);


--
-- Name: pessoas pessoas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pessoas
    ADD CONSTRAINT pessoas_pkey PRIMARY KEY (cpf);


--
-- Name: salas salas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_pkey PRIMARY KEY (numero_sala);


--
-- Name: sessoes sessoes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes
    ADD CONSTRAINT sessoes_pkey PRIMARY KEY (id);


--
-- Name: bilhetes bilhetes_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bilhetes
    ADD CONSTRAINT bilhetes_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES public.clientes(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bilhetes bilhetes_funcionario_vendedor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bilhetes
    ADD CONSTRAINT bilhetes_funcionario_vendedor_id_fkey FOREIGN KEY (funcionario_vendedor_id) REFERENCES public.funcionarios(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bilhetes bilhetes_sessao_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bilhetes
    ADD CONSTRAINT bilhetes_sessao_id_fkey FOREIGN KEY (sessao_id) REFERENCES public.sessoes(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: clientes clientes_cpf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_cpf_fkey FOREIGN KEY (cpf) REFERENCES public.pessoas(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: funcionarios funcionarios_cpf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_cpf_fkey FOREIGN KEY (cpf) REFERENCES public.pessoas(cpf) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: generos_filmes generos_filmes_filme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos_filmes
    ADD CONSTRAINT generos_filmes_filme_id_fkey FOREIGN KEY (filme_id) REFERENCES public.filmes(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: generos_filmes generos_filmes_genero_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generos_filmes
    ADD CONSTRAINT generos_filmes_genero_fkey FOREIGN KEY (genero) REFERENCES public.generos(nome) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: sessoes sessoes_filme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes
    ADD CONSTRAINT sessoes_filme_id_fkey FOREIGN KEY (filme_id) REFERENCES public.filmes(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: sessoes sessoes_numero_sala_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessoes
    ADD CONSTRAINT sessoes_numero_sala_fkey FOREIGN KEY (numero_sala) REFERENCES public.salas(numero_sala) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

