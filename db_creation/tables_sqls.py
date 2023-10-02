tables_sqls = ['''CREATE TABLE filmes(
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    data_estreia DATE NOT NULL,
                    pais_origem VARCHAR(30) NOT NULL,
                    duracao INTERVAL NOT NULL,
                    direcao VARCHAR(255) NOT NULL,
                    faixa_etaria VARCHAR(10) NOT NULL)''',
                '''CREATE TABLE generos(
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL)''',
                '''CREATE TABLE generos_filmes(
                    filme_id INT NOT NULL,
                    genero_id INT NOT NULL,
                    PRIMARY KEY (filme_id, genero_id),
                    FOREIGN KEY (filme_id)
                        REFERENCES filmes (id),
                    FOREIGN KEY (genero_id)
                        REFERENCES generos (id))''',
                '''CREATE TABLE salas(
                    id SERIAL PRIMARY KEY,
                    numero_cadeiras INT NOT NULL,
                    tamanho_tela VARCHAR(10) NOT NULL,
                    capacidade_maxima INT NOT NULL,
                    tridimensional BOOLEAN NOT NULL,
                    vip BOOLEAN NOT NULL)''',
                '''CREATE TABLE sessoes(
                    id SERIAL PRIMARY KEY,
                    filme_id INT NOT NULL,
                    numero_sala INT NOT NULL,
                    data TIMESTAMP NOT NULL,
                    faixa_audio VARCHAR(30) NOT NULL,
                    legenda BOOLEAN NOT NULL,
                    FOREIGN KEY (filme_id)
                        REFERENCES filmes (id),
                    FOREIGN KEY (numero_sala)
                        REFERENCES salas (id))''',
                '''CREATE TABLE bilhetes(
                    id SERIAL PRIMARY KEY,
                    sessao_id INT NOT NULL,
                    data_compra TIMESTAMP NOT NULL,
                    valor_compra MONEY NOT NULL,
                    FOREIGN KEY (sessao_id)
                        REFERENCES sessoes (id))''']