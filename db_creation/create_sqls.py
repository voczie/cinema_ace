tables_sqls = ['''CREATE TABLE filmes(
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    data_estreia DATE NOT NULL,
                    pais_origem VARCHAR(30) NOT NULL,
                    duracao INTERVAL NOT NULL,
                    direcao VARCHAR(255) NOT NULL,
                    faixa_etaria VARCHAR(10) NOT NULL,
                    gravado_mari BOOLEAN NOT NULL)''',

                '''CREATE TABLE generos(
                    nome VARCHAR(255) PRIMARY KEY)''',

                '''CREATE TABLE generos_filmes(
                    filme_id INT NOT NULL,
                    genero VARCHAR(255) NOT NULL,
                    PRIMARY KEY (filme_id, genero),
                    FOREIGN KEY (filme_id)
                        REFERENCES filmes (id),
                    FOREIGN KEY (genero)
                        REFERENCES generos (nome))''',

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
                    qnt_bilhetes_disponivel INT NOT NULL,
                    preco_inteira MONEY NOT NULL,
                    FOREIGN KEY (filme_id)
                        REFERENCES filmes (id),
                    FOREIGN KEY (numero_sala)
                        REFERENCES salas (id))''',

                '''CREATE TABLE pessoas(
                    cpf VARCHAR(11) PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    idade INT NOT NULL,
                    login VARCHAR(60) NOT NULL UNIQUE,
                    senha VARCHAR(60) NOT NULL)''',

                '''CREATE TABLE funcionarios(
                    cpf VARCHAR(11) PRIMARY KEY,
                    salario MONEY NOT NULL,
                    FOREIGN KEY (cpf)
                        REFERENCES pessoas (cpf))''',

                '''CREATE TABLE clientes(
                    cpf VARCHAR(11) PRIMARY KEY,
                    flamenguista BOOLEAN NOT NULL,
                    assiste_onepiece BOOLEAN NOT NULL,
                    sousense BOOLEAN NOT NULL,
                    FOREIGN KEY (cpf)
                        REFERENCES pessoas (cpf))''',

                '''CREATE TABLE bilhetes(
                    id SERIAL PRIMARY KEY,
                    sessao_id INT NOT NULL,
                    funcionario_vendedor_id VARCHAR(11) NOT NULL,
                    cliente_id VARCHAR(11) NOT NULL,
                    compra_concluida BOOLEAN NOT NULL,
                    data_compra TIMESTAMP NOT NULL,
                    preco_pago MONEY NOT NULL,
                    tipo_pagamento VARCHAR(25) NOT NULL,
                    FOREIGN KEY (sessao_id)
                        REFERENCES sessoes (id),
                    FOREIGN KEY (funcionario_vendedor_id)
                        REFERENCES funcionarios (cpf),
                    FOREIGN KEY (cliente_id)
                        REFERENCES clientes (cpf))'''
]