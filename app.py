# -*- coding: utf-8 -*-
"""
Sistema de Gerenciamento de Logs e Relatórios Internos
Aplicação desenvolvida para gestão e análise de registros operacionais
"""

import streamlit as st
import random
from datetime import datetime

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="Sistema de Gerenciamento de Logs e Relatórios Internos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== DADOS DAS QUESTÕES ====================
QUESTOES = [
    # CRIMES CONTRA A FÉ PÚBLICA - FALSIFICAÇÃO DE DOCUMENTOS
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Qual a pena prevista no art. 297 do Código Penal para o crime de falsificação de documento público?",
        "resposta": "Reclusão, de 2 (dois) a 6 (seis) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Se o agente é funcionário público e comete o crime de falsificação de documento público prevalecendo-se do cargo, qual é a consequência prevista no art. 297, §1º do CP?",
        "resposta": "A pena é aumentada de sexta parte."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Durante uma fiscalização de trânsito, o motorista apresenta CNH falsificada. Qual crime está configurado no art. 304 do CP?",
        "resposta": "Uso de documento falso. A pena é a mesma prevista para a falsificação ou alteração do documento."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "O que caracteriza o crime de falsidade ideológica previsto no art. 299 do CP?",
        "resposta": "Omitir, em documento público ou particular, declaração que dele devia constar, ou nele inserir ou fazer inserir declaração falsa ou diversa da que devia ser escrita, com o fim de prejudicar direito, criar obrigação ou alterar a verdade sobre fato juridicamente relevante."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Qual a pena para o crime de falsidade ideológica (art. 299, CP)?",
        "resposta": "Reclusão, de 1 (um) a 5 (cinco) anos, e multa, se o documento é público, e de 1 (um) a 3 (três) anos, e multa, se o documento é particular."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Um motorista adultera o número do chassi de seu veículo. Qual crime está previsto no art. 311 do CP?",
        "resposta": "Adulteração de sinal identificador de veículo automotor. Pena: reclusão, de 3 (três) a 6 (seis) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Durante abordagem, o motorista apresenta documento de identidade de outra pessoa como se fosse seu. Qual crime está configurado no art. 308 do CP?",
        "resposta": "Uso de documento de identidade alheio. Pena: detenção, de 4 (quatro) meses a 2 (dois) anos, e multa, se o fato não constitui elemento de crime mais grave."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "O que caracteriza o crime de falsa identidade previsto no art. 307 do CP?",
        "resposta": "Atribuir-se ou atribuir a terceiro falsa identidade para obter vantagem, em proveito próprio ou alheio, ou para causar dano a outrem. Pena: detenção, de 3 (três) meses a 1 (um) ano, ou multa."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Um motorista, ao ser abordado, fornece nome falso ao agente de trânsito. Qual crime pode estar configurado?",
        "resposta": "Falsa identidade (art. 307, CP), se o fato não constituir elemento de crime mais grave."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Qual a pena para o crime de falsificação de documento particular previsto no art. 298 do CP?",
        "resposta": "Reclusão, de 1 (um) a 5 (cinco) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "O crime de supressão de documento público está previsto em qual artigo do CP e qual sua pena?",
        "resposta": "Art. 305 do CP. Pena: reclusão, de 2 (dois) a 6 (seis) anos, e multa, se o documento é público, e reclusão, de 1 (um) a 5 (cinco) anos, e multa, se o documento é particular."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Durante fiscalização, o agente descobre que o motorista está portando petrechos destinados à falsificação de documentos. Qual crime está previsto no art. 294 do CP?",
        "resposta": "Petrechos de falsificação. Pena: reclusão, de 1 (um) a 3 (três) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Se um funcionário público comete crime de petrechos de falsificação prevalecendo-se do cargo, qual a consequência prevista no art. 295 do CP?",
        "resposta": "A pena aumenta-se de sexta parte."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "O que caracteriza o crime de fraude em certames de interesse público previsto no art. 311-A do CP?",
        "resposta": "Utilizar ou divulgar, indevidamente, com o fim de beneficiar a si ou a outrem, ou de comprometer a credibilidade do certame, conteúdo sigiloso de concurso público, avaliação ou exame públicos, processo seletivo para ingresso no ensino superior, ou exame ou processo seletivo previstos em lei."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Qual a pena para o crime de fraude em certames de interesse público (art. 311-A, CP)?",
        "resposta": "Reclusão, de 1 (um) a 4 (quatro) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "O crime de uso de documento falso (art. 304, CP) tem pena própria?",
        "resposta": "Não. A pena é a mesma prevista para a falsificação ou alteração do documento."
    },
    {
        "categoria": "Crimes contra a Fé Pública",
        "pergunta": "Reconhecer, como verdadeira, no exercício de função pública, firma ou letra que não seja configura qual crime?",
        "resposta": "Falso reconhecimento de firma ou letra (art. 300, CP). Pena: reclusão, de 1 (um) a 5 (cinco) anos, e multa, se o documento é público, e de 1 (um) a 3 (três) anos, e multa, se o documento é particular."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - PECULATO
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de peculato apropriação previsto no art. 312, caput, 1ª parte do CP?",
        "resposta": "O funcionário público apropria-se de dinheiro, valor ou qualquer outro bem móvel, público ou particular, de que tem a posse em razão do cargo."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a diferença entre peculato apropriação e peculato desvio?",
        "resposta": "No peculato apropriação, o funcionário toma para si o bem que possui em virtude do cargo. No peculato desvio, o funcionário desvia o bem para uma finalidade diversa daquela que lhe foi determinada."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o peculato furto previsto no art. 312, §1º do CP?",
        "resposta": "O funcionário público subtrai dolosamente um bem que não possui a posse, para usar em proveito próprio ou alheio."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena prevista para o crime de peculato (art. 312, CP)?",
        "resposta": "Reclusão, de 2 (dois) a 12 (doze) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O peculato pode ser culposo? Se sim, qual a pena?",
        "resposta": "Sim. O peculato culposo está previsto no art. 312, §2º do CP. Pena: detenção, de 3 (três) meses a 1 (um) ano."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O crime de peculato mediante erro de outrem está previsto em qual artigo do CP?",
        "resposta": "Art. 313 do CP."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Inserir ou facilitar a inserção de dados falsos em sistema de informações da Administração Pública configura qual crime?",
        "resposta": "Peculato eletrônico (art. 313-A, CP)."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - CONCUSSÃO E CORRUPÇÃO
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de concussão previsto no art. 316 do CP?",
        "resposta": "Exigir, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de concussão (art. 316, CP)?",
        "resposta": "Reclusão, de 2 (dois) a 12 (doze) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Durante uma fiscalização de trânsito, o agente EXIGE do motorista R$ 200,00 para não aplicar a multa. Qual crime está configurado?",
        "resposta": "Concussão (art. 316, CP), pois o verbo nuclear é 'exigir', caracterizando intimidação."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de corrupção passiva previsto no art. 317 do CP?",
        "resposta": "Solicitar ou receber, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida, ou aceitar promessa de tal vantagem."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de corrupção passiva (art. 317, CP)?",
        "resposta": "Reclusão, de 2 (dois) a 12 (doze) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a principal diferença entre concussão e corrupção passiva?",
        "resposta": "Na concussão, o verbo é 'exigir' (caráter intimidativo). Na corrupção passiva, o verbo é 'solicitar' ou 'receber' (não há intimidação)."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Um agente de trânsito SOLICITA ao motorista R$ 100,00 para não lavrar o auto de infração. Qual crime está configurado?",
        "resposta": "Corrupção passiva (art. 317, CP), pois o verbo nuclear é 'solicitar'."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza a corrupção passiva privilegiada prevista no art. 317, §2º do CP?",
        "resposta": "O funcionário público pratica, deixa de praticar ou retarda ato de ofício, com infração de dever funcional, cedendo a pedido ou influência de outrem."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para a corrupção passiva privilegiada (art. 317, §2º, CP)?",
        "resposta": "Detenção, de 3 (três) meses a 1 (um) ano, ou multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de corrupção ativa previsto no art. 333 do CP?",
        "resposta": "Oferecer ou prometer vantagem indevida a funcionário público, para determiná-lo a praticar, omitir ou retardar ato de ofício."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de corrupção ativa (art. 333, CP)?",
        "resposta": "Reclusão, de 2 (dois) a 12 (doze) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Durante fiscalização, o motorista oferece R$ 500,00 ao agente de trânsito para não ser multado. Qual crime o motorista cometeu?",
        "resposta": "Corrupção ativa (art. 333, CP)."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - PREVARICAÇÃO
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de prevaricação previsto no art. 319 do CP?",
        "resposta": "Retardar ou deixar de praticar, indevidamente, ato de ofício, ou praticá-lo contra disposição expressa de lei, para satisfazer interesse ou sentimento pessoal."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de prevaricação (art. 319, CP)?",
        "resposta": "Detenção, de 3 (três) meses a 1 (um) ano, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a diferença entre prevaricação e corrupção passiva privilegiada?",
        "resposta": "Na prevaricação, o funcionário pratica a conduta para satisfazer interesse ou sentimento pessoal. Na corrupção passiva privilegiada, ele pratica cedendo a pedido ou influência de outrem."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Um agente de trânsito deixa de autuar seu amigo por excesso de velocidade para satisfazer interesse pessoal. Qual crime está configurado?",
        "resposta": "Prevaricação (art. 319, CP)."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Um agente de trânsito retarda propositalmente a lavratura de auto de infração contra desafeto pessoal, agravando sua situação. Qual crime pode estar configurado?",
        "resposta": "Prevaricação (art. 319, CP), pois retardou ato de ofício para satisfazer sentimento pessoal."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - CONDESCENDÊNCIA CRIMINOSA
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de condescendência criminosa previsto no art. 320 do CP?",
        "resposta": "O funcionário deixa, por indulgência (tolerância/clemência), de responsabilizar subordinado que cometeu infração no exercício do cargo ou, quando lhe competir, não levar o fato ao conhecimento da autoridade competente."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de condescendência criminosa (art. 320, CP)?",
        "resposta": "Detenção, de 15 (quinze) dias a 1 (um) mês, ou multa."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - EXCESSO DE EXAÇÃO
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de excesso de exação previsto no art. 316, §1º do CP?",
        "resposta": "O funcionário exige tributo ou contribuição social que sabe ou deveria saber indevido, ou, quando devido, emprega na cobrança meio vexatório ou gravoso, que a lei não autoriza."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de excesso de exação (art. 316, §1º, CP)?",
        "resposta": "Reclusão, de 3 (três) a 8 (oito) anos, e multa."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - USURPAÇÃO
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de usurpação da função pública previsto no art. 328 do CP?",
        "resposta": "O particular finge ser funcionário público e pratica atos inerentes à função, mesmo sem aprovação em concurso ou nomeação."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de usurpação da função pública (art. 328, CP)?",
        "resposta": "Detenção, de 3 (três) meses a 2 (dois) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Um particular se veste de agente de trânsito e realiza fiscalizações. Qual crime está configurado?",
        "resposta": "Usurpação da função pública (art. 328, CP)."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - RESISTÊNCIA, DESOBEDIÊNCIA E DESACATO
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de resistência previsto no art. 329 do CP?",
        "resposta": "Opor-se à execução de ato legal, mediante violência ou ameaça a funcionário competente para executá-lo ou a quem lhe esteja prestando auxílio."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de resistência (art. 329, CP)?",
        "resposta": "Detenção, de 2 (dois) meses a 2 (dois) anos."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Durante abordagem, o motorista empurra o agente de trânsito e tenta fugir. Qual crime está configurado?",
        "resposta": "Resistência (art. 329, CP), pois houve violência para opor-se à execução de ato legal."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de desobediência previsto no art. 330 do CP?",
        "resposta": "Desobedecer a ordem legal de funcionário público."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de desobediência (art. 330, CP)?",
        "resposta": "Detenção, de 15 (quinze) dias a 6 (seis) meses, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O agente de trânsito ordena ao motorista que estacione o veículo para fiscalização, mas o motorista ignora e segue viagem. Qual crime pode estar configurado?",
        "resposta": "Desobediência (art. 330, CP), se a ordem era legal."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de desacato previsto no art. 331 do CP?",
        "resposta": "Desacatar funcionário público no exercício da função ou em razão dela."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de desacato (art. 331, CP)?",
        "resposta": "Detenção, de 6 (seis) meses a 2 (dois) anos, ou multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Durante fiscalização, o motorista xinga e ofende o agente de trânsito. Qual crime está configurado?",
        "resposta": "Desacato (art. 331, CP)."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Para configurar o crime de desacato, é necessário que o agente saiba que a vítima é funcionário público?",
        "resposta": "Sim. O agente deve saber que a vítima é funcionário público, pois, se não souber, o dolo está afastado."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a diferença entre resistência e desobediência?",
        "resposta": "Na resistência, há violência ou ameaça para opor-se à execução de ato legal. Na desobediência, há simplesmente o descumprimento de ordem legal, sem violência."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - TRÁFICO DE INFLUÊNCIA
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de tráfico de influência previsto no art. 332 do CP?",
        "resposta": "Solicitar, exigir, cobrar ou obter, para si ou para outrem, vantagem ou promessa de vantagem, a pretexto de influir em ato praticado por funcionário público no exercício da função."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de tráfico de influência (art. 332, CP)?",
        "resposta": "Reclusão, de 2 (dois) a 5 (cinco) anos, e multa."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - DESCAMINHO E CONTRABANDO
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de descaminho previsto no art. 334 do CP?",
        "resposta": "Iludir, no todo ou em parte, o pagamento de direito ou imposto devido pela entrada, pela saída ou pelo consumo de mercadoria."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de descaminho (art. 334, CP)?",
        "resposta": "Reclusão, de 1 (um) a 4 (quatro) anos."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de contrabando previsto no art. 334-A do CP?",
        "resposta": "Importar ou exportar mercadoria proibida."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de contrabando (art. 334-A, CP)?",
        "resposta": "Reclusão, de 2 (dois) a 5 (cinco) anos."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a diferença entre descaminho e contrabando?",
        "resposta": "No descaminho, ocorre a entrada e saída de mercadorias legais, mas que não recolheram os impostos devidos. No contrabando, as mercadorias são ilegais (proibidas por lei)."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - DENUNCIAÇÃO CALUNIOSA
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de denunciação caluniosa previsto no art. 339 do CP?",
        "resposta": "Dar causa à instauração de inquérito policial, de procedimento investigatório criminal, de processo judicial, de processo administrativo disciplinar, de inquérito civil ou de ação de improbidade administrativa contra alguém, imputando-lhe crime, infração ético-disciplinar ou ato de improbidade que o agente sabe inocente."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de denunciação caluniosa (art. 339, CP)?",
        "resposta": "Reclusão, de 2 (dois) a 8 (oito) anos, e multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Um motorista registra ocorrência policial falsa contra agente de trânsito, imputando-lhe crime que sabe não ter ocorrido. Qual crime está configurado?",
        "resposta": "Denunciação caluniosa (art. 339, CP)."
    },

    # CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA - COMUNICAÇÃO FALSA
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "O que caracteriza o crime de comunicação falsa de crime ou contravenção previsto no art. 340 do CP?",
        "resposta": "Provocar a ação de autoridade, comunicando-lhe a ocorrência de crime ou de contravenção que sabe não se ter verificado."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a pena para o crime de comunicação falsa de crime ou contravenção (art. 340, CP)?",
        "resposta": "Detenção, de 1 (um) a 6 (seis) meses, ou multa."
    },
    {
        "categoria": "Crimes contra a Administração Pública",
        "pergunta": "Qual a diferença entre denunciação caluniosa e comunicação falsa de crime?",
        "resposta": "Na denunciação caluniosa, há imputação de crime contra pessoa determinada. Na comunicação falsa, o agente limita-se a narrar à autoridade infração inexistente, sem identificar seu autor."
    },

    # QUESTÕES MISTAS E SITUAÇÕES PRÁTICAS
    {
        "categoria": "Situações Práticas",
        "pergunta": "Durante fiscalização de trânsito, o motorista apresenta CNH com foto adulterada. Quais crimes podem estar configurados?",
        "resposta": "Falsificação de documento público (art. 297, CP) e uso de documento falso (art. 304, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um agente de trânsito, durante fiscalização, recebe proposta de R$ 300,00 de um motorista para não lavrar auto de infração. O agente aceita o dinheiro. Quais crimes foram cometidos?",
        "resposta": "O motorista cometeu corrupção ativa (art. 333, CP) e o agente cometeu corrupção passiva (art. 317, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Durante abordagem, o motorista se recusa a apresentar documentos e empurra o agente. Quais crimes podem estar configurados?",
        "resposta": "Desobediência (art. 330, CP) e resistência (art. 329, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um agente de trânsito exige R$ 500,00 de um motorista sob ameaça de apreender o veículo. Qual crime o agente cometeu?",
        "resposta": "Concussão (art. 316, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Durante fiscalização, o motorista oferece bebida alcoólica ao agente e diz: 'Vamos resolver isso de outro jeito'. O agente recusa. Qual crime o motorista tentou cometer?",
        "resposta": "Tentativa de corrupção ativa (art. 333, CP c/c art. 14, II, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um motorista é flagrado com placa de veículo adulterada. Qual crime está configurado?",
        "resposta": "Adulteração de sinal identificador de veículo automotor (art. 311, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Durante abordagem, o motorista grita ofensas ao agente de trânsito e o chama de incompetente. Qual crime está configurado?",
        "resposta": "Desacato (art. 331, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um agente de trânsito deixa de autuar motorista que cometeu infração grave, pois o motorista é seu primo. Qual crime está configurado?",
        "resposta": "Prevaricação (art. 319, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Durante fiscalização, o motorista apresenta documento de habilitação de outra pessoa. Qual crime está configurado?",
        "resposta": "Uso de documento de identidade alheio (art. 308, CP) ou uso de documento falso (art. 304, CP), dependendo do contexto."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um agente de trânsito solicita ao motorista que lhe pague R$ 200,00 para evitar a multa. Qual crime está configurado?",
        "resposta": "Corrupção passiva (art. 317, CP)."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um motorista, ao ser abordado, tenta subornar o agente oferecendo dinheiro. O agente recusa. Houve crime consumado?",
        "resposta": "Sim. O crime de corrupção ativa se consuma com a simples oferta ou promessa de vantagem indevida, independentemente da aceitação."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um agente de trânsito solicita vantagem indevida, mas o motorista recusa. Houve crime consumado?",
        "resposta": "Sim. O crime de corrupção passiva se consuma com a simples solicitação, independentemente do recebimento da vantagem."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Durante fiscalização, o motorista foge em alta velocidade ao avistar a blitz. Qual crime pode estar configurado?",
        "resposta": "Desobediência (art. 330, CP), se houve ordem de parada, ou apenas infração de trânsito, dependendo das circunstâncias."
    },
    {
        "categoria": "Situações Práticas",
        "pergunta": "Um agente de trânsito aplica multa indevida a desafeto pessoal, mesmo sabendo que não houve infração. Qual crime está configurado?",
        "resposta": "Prevaricação (art. 319, CP)."
    },

    # CONCEITOS FUNDAMENTAIS
    {
        "categoria": "Conceitos Fundamentais",
        "pergunta": "Para fins penais, quem é considerado funcionário público conforme o art. 327 do CP?",
        "resposta": "Considera-se funcionário público, para os efeitos penais, quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública."
    },
    {
        "categoria": "Conceitos Fundamentais",
        "pergunta": "Equipara-se a funcionário público, para fins penais, quem exerce função em qual tipo de entidade?",
        "resposta": "Equipara-se a funcionário público quem exerce cargo, emprego ou função em entidade paraestatal, e quem trabalha para empresa prestadora de serviço contratada ou conveniada para a execução de atividade típica da Administração Pública."
    },
    {
        "categoria": "Conceitos Fundamentais",
        "pergunta": "Um agente de trânsito terceirizado pode ser considerado funcionário público para fins penais?",
        "resposta": "Sim, pois equipara-se a funcionário público quem trabalha para empresa prestadora de serviço contratada para execução de atividade típica da Administração Pública (art. 327, §1º, CP)."
    },
    {
        "categoria": "Conceitos Fundamentais",
        "pergunta": "Todos os crimes contra a administração pública praticados por funcionário público são dolosos?",
        "resposta": "Não. A maioria é dolosa, mas o peculato admite a modalidade culposa (art. 312, §2º, CP)."
    },
    {
        "categoria": "Conceitos Fundamentais",
        "pergunta": "Qual é o único crime contra a administração pública que admite a modalidade culposa?",
        "resposta": "Peculato culposo (art. 312, §2º, CP)."
    },

    # QUESTÕES SOBRE PENAS E AGRAVANTES
    {
        "categoria": "Penas e Agravantes",
        "pergunta": "Quando o funcionário público comete crime de falsificação prevalecendo-se do cargo, qual é a consequência?",
        "resposta": "A pena é aumentada de sexta parte (art. 295 e 297, §1º, CP)."
    },
    {
        "categoria": "Penas e Agravantes",
        "pergunta": "Qual crime tem pena mais grave: concussão ou corrupção passiva?",
        "resposta": "Ambos têm a mesma pena: reclusão, de 2 (dois) a 12 (doze) anos, e multa."
    },
    {
        "categoria": "Penas e Agravantes",
        "pergunta": "Qual crime tem pena mais branda: prevaricação ou corrupção passiva privilegiada?",
        "resposta": "Ambos têm a mesma pena: detenção, de 3 (três) meses a 1 (um) ano, e multa (ou multa isoladamente na corrupção passiva privilegiada)."
    },
    {
        "categoria": "Penas e Agravantes",
        "pergunta": "Qual crime tem pena mais grave: resistência ou desacato?",
        "resposta": "Desacato (detenção de 6 meses a 2 anos) tem pena mais grave que resistência (detenção de 2 meses a 2 anos)."
    },
    {
        "categoria": "Penas e Agravantes",
        "pergunta": "Qual crime tem pena mais branda: desobediência ou condescendência criminosa?",
        "resposta": "Condescendência criminosa (detenção de 15 dias a 1 mês) tem pena mais branda que desobediência (detenção de 15 dias a 6 meses)."
    },

    # QUESTÕES SOBRE ABUSO DE AUTORIDADE (Lei 13.869/2019)
    {
        "categoria": "Abuso de Autoridade",
        "pergunta": "A Lei 13.869/2019 trata de qual tema?",
        "resposta": "Abuso de autoridade."
    },
    {
        "categoria": "Abuso de Autoridade",
        "pergunta": "Um agente de trânsito que, sem justa causa, submete pessoa sob sua guarda a vexame ou constrangimento pode responder por qual crime?",
        "resposta": "Abuso de autoridade, conforme Lei 13.869/2019."
    },
    {
        "categoria": "Abuso de Autoridade",
        "pergunta": "Constranger o preso ou o detento, mediante violência, grave ameaça ou redução de sua capacidade de resistência, a exibir-se ou ter seu corpo ou parte dele exibido à curiosidade pública configura qual crime?",
        "resposta": "Abuso de autoridade (Lei 13.869/2019)."
    },
    {
        "categoria": "Abuso de Autoridade",
        "pergunta": "Proceder à obtenção de prova, em procedimento de investigação ou fiscalização, por meio manifestamente ilícito configura qual crime?",
        "resposta": "Abuso de autoridade (Lei 13.869/2019)."
    },
]

# ==================== ESTILO CSS PERSONALIZADO ====================
st.markdown("""
<style>
    /* Tema corporativo discreto */
    .main {
        background-color: #f5f5f5;
    }
    
    /* Cabeçalho profissional */
    .header-style {
        background: linear-gradient(135deg, #1e3a5f 0%, #2c5282 100%);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .header-title {
        color: white;
        font-size: 28px;
        font-weight: 600;
        margin: 0;
        text-align: center;
    }
    
    .header-subtitle {
        color: #e0e0e0;
        font-size: 14px;
        text-align: center;
        margin-top: 8px;
    }
    
    /* Card de registro */
    .registro-card {
        background-color: white;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border-left: 4px solid #2c5282;
    }
    
    .registro-id {
        color: #1e3a5f;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .registro-conteudo {
        color: #333;
        font-size: 18px;
        line-height: 1.6;
        margin-bottom: 20px;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 6px;
        border: 1px solid #e0e0e0;
    }
    
    .detalhes-log {
        background-color: #e8f4f8;
        padding: 20px;
        border-radius: 6px;
        border-left: 4px solid #0066cc;
        margin-top: 20px;
    }
    
    .detalhes-titulo {
        color: #1e3a5f;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    
    .detalhes-conteudo {
        color: #2c3e50;
        font-size: 16px;
        line-height: 1.7;
    }
    
    /* Botões corporativos */
    .stButton>button {
        background-color: #2c5282;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 12px 24px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #1e3a5f;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Sidebar corporativa */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Métricas */
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 6px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        text-align: center;
        margin-bottom: 15px;
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: 700;
        color: #2c5282;
    }
    
    .metric-label {
        font-size: 12px;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INICIALIZAÇÃO DO SESSION STATE ====================
if 'questao_atual' not in st.session_state:
    st.session_state.questao_atual = None
    st.session_state.mostrar_resposta = False
    st.session_state.categoria_filtro = "Todas"
    st.session_state.contador_registros = 0

# ==================== FUNÇÕES AUXILIARES ====================
def gerar_nova_questao(categoria_filtro="Todas"):
    """Gera uma nova questão aleatória"""
    if categoria_filtro == "Todas":
        questoes_disponiveis = QUESTOES
    else:
        questoes_disponiveis = [q for q in QUESTOES if q["categoria"] == categoria_filtro]
    
    if questoes_disponiveis:
        st.session_state.questao_atual = random.choice(questoes_disponiveis)
        st.session_state.mostrar_resposta = False
        st.session_state.contador_registros += 1

def obter_categorias():
    """Retorna lista de categorias únicas"""
    categorias = list(set([q["categoria"] for q in QUESTOES]))
    return ["Todas"] + sorted(categorias)

# ==================== CABEÇALHO ====================
st.markdown("""
<div class="header-style">
    <h1 class="header-title">📊 Sistema de Gerenciamento de Logs e Relatórios Internos</h1>
    <p class="header-subtitle">Versão 2.1.4 | Módulo de Análise e Consulta de Registros Operacionais</p>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### ⚙️ Configurações do Sistema")
    st.markdown("---")
    
    # Filtro de "Departamento" (na verdade, categoria)
    st.markdown("#### 📁 Filtros de Relatório")
    
    categorias = obter_categorias()
    categoria_selecionada = st.selectbox(
        "Departamento:",
        categorias,
        key="categoria_select"
    )
    st.session_state.categoria_filtro = categoria_selecionada
    
    # Filtro de período (fictício, apenas visual)
    st.selectbox(
        "Período do Relatório:",
        ["Último Trimestre", "Último Semestre", "Último Ano", "Todos os Períodos"],
        index=3
    )
    
    st.markdown("---")
    
    # Estatísticas
    st.markdown("#### 📈 Estatísticas")
    
    total_questoes = len(QUESTOES)
    if categoria_selecionada == "Todas":
        questoes_filtradas = total_questoes
    else:
        questoes_filtradas = len([q for q in QUESTOES if q["categoria"] == categoria_selecionada])
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{total_questoes}</div>
        <div class="metric-label">Total de Registros</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{questoes_filtradas}</div>
        <div class="metric-label">Registros Filtrados</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{st.session_state.contador_registros}</div>
        <div class="metric-label">Consultas Realizadas</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Informações do sistema
    st.markdown("#### ℹ️ Informações do Sistema")
    st.markdown(f"""
    <small>
    **Data/Hora:** {datetime.now().strftime('%d/%m/%Y %H:%M')}<br>
    **Usuário:** Admin<br>
    **Status:** ✅ Online
    </small>
    """, unsafe_allow_html=True)

# ==================== ÁREA PRINCIPAL ====================

# Botão para gerar novo registro
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔄 Próximo Registro", use_container_width=True):
        gerar_nova_questao(st.session_state.categoria_filtro)

# Se não houver questão atual, gerar uma
if st.session_state.questao_atual is None:
    gerar_nova_questao(st.session_state.categoria_filtro)

# Exibir questão atual
if st.session_state.questao_atual:
    questao = st.session_state.questao_atual
    
    st.markdown(f"""
    <div class="registro-card">
        <div class="registro-id">📋 ID do Registro: REG-{st.session_state.contador_registros:04d}</div>
        <div class="registro-conteudo">
            {questao['pergunta']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão para verificar status (revelar resposta)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Verificar Status", use_container_width=True):
            st.session_state.mostrar_resposta = True
    
    # Exibir resposta se solicitado
    if st.session_state.mostrar_resposta:
        st.markdown(f"""
        <div class="detalhes-log">
            <div class="detalhes-titulo">📄 Detalhes do Log</div>
            <div class="detalhes-conteudo">
                {questao['resposta']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Informações adicionais (metadados fictícios)
        st.markdown("---")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**Categoria:** {questao['categoria']}")
        with col_b:
            st.markdown(f"**Timestamp:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# Rodapé
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px; padding: 20px;'>
    Sistema de Gerenciamento de Logs e Relatórios Internos v2.1.4<br>
    © 2025 - Todos os direitos reservados | Departamento de TI
</div>
""", unsafe_allow_html=True)
