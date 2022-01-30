import discord
import os
import random


client = discord.Client()

textosEmCasoDe = [
    'Em caso de investigação policial, eu oficialmente declaro que não tenho envolvimento com este grupo e não sei como estou no mesmo, provavelmente fui inserido por terceiros, declaro que estou disposto a colaborar com as investigações e estou disposto a me apresentar a depoimento se necessário, declaro que sou completamente inocente e não tenho envolvimento nenhum com este caso mostrado neste post específico.',
    'In case of police investigation, I officially declare that I have no involvement with this group and do not know how I am in it, I was probably inserted by third parties, declare that I am willing to cooperate with the investigation and am willing to introduce me to testimony if necessary, I declare that I am completely innocent and have no involvement with this case no shown in this particular post.',
    '警察の捜査のケースでは、私は正式に、私はこのグループと何の関わりを持っていないと私は調査に協力して喜んで、必要に応じて証言に私を紹介して喜んでいることを宣言し、私はおそらく第三者によって挿入された、私はそれで午前のか分からないことを宣言します私は完全に無実だとなし、この特定のポストに示す。この場合とは関わりがないことを宣言します。',
    'Bei polizeilichen Ermittlungen erkläre ich offiziell, dass ich keine Beteiligung an dieser Gruppe haben und nicht wissen, wie ich es bin, ich wahrscheinlich von Dritten eingesetzt wurde, erklären, dass ich bereit bin, mit der Untersuchung mitzuarbeiten und bin bereit, mich wenn nötig Zeugnis einzuführen, ich erkläre, dass ich bin völlig unschuldig und habe keine Beteiligung mit diesem Fall nicht in diesem Beitrag gezeigt.',
    'В случае полицейского расследования, я официально заявляю, что я не имею никакого отношения с этой группой и не знаю, как я в этом, я, вероятно, был вставлен третьими лицами, заявить, что я готов сотрудничать со следствием и готов познакомить меня с показаниями в случае необходимости, Я заявляю, что я абсолютно невиновен и не имеют никакого отношения с этим делом не показанным на данном посту.',
    '在警方調查的情況下，我正式宣布我有這個組不參與，不知道怎麼我在呢，我可能是由第三方插入聲明，我願意與配合調查，我願意在必要時把我介紹給證詞，我聲明，我是完全無辜的，並與這種情況下，在這個特殊的崗位沒有顯示任何參與。',
    'Dans le cas d\'une enquête policière, je déclare officiellement que je ne participe pas à ce groupe et je ne sais pas comment je suis dedans, je suis probablement inséré par des tiers, déclare que je suis prêt à coopérer avec l\'enquête et je suis prêt à me présenter au témoignage si nécessaire, Je déclare que je suis complètement innocent et ne participera pas à cette affaire ne montre dans ce poste particulier.',
    'Si vigilum quaestionem et publice testari nihil concursus cum istis et nescio ego in ea sum probabiliter interpretibus alios ostendunt volo cooperari cognitione volo afferre mihi testimonium, si necesse fuerit, summe innocens ego sum et non indicans quaedam post hoc nullum est in hac parte.',
    'ในกรณีของการสืบสวนของตำรวจผมอย่างเป็นทางการประกาศว่าผมมีส่วนร่วมกับกลุ่มนี้และไม่ทราบว่าผมกำลังอยู่ในนั้นผมอาจจะเขียนโดยบุคคลที่สามประกาศว่าฉันยินดีที่จะให้ความร่วมมือกับการสอบสวนและยินดีที่จะแนะนำให้ฉันไปพยานหลักฐานในกรณีที่จำเป็น ผมประกาศว่าผมเป็นผู้บริสุทธิ์อย่างสมบูรณ์และไม่มีส่วนร่วมกับกรณีนี้ไม่มีการแสดงในโพสต์นี้โดยเฉพาะอย่',
    'Ved politietterforskning , jeg offisielt erklære at jeg ikke har noen befatning med denne gruppen, og vet ikke hvordan jeg i det, jeg var trolig satt av tredjeparter , erklærer at jeg er villig til å samarbeide med etterforskningen og er villig til å introdusere meg til vitnesbyrd om nødvendig, jeg erklærer at jeg er helt uskyldig og har ingen befatning med denne saken ikke vist i dette innlegget.',
    'Στην περίπτωση της αστυνομικής έρευνας, εγώ επίσημα δηλώσει ότι δεν έχω καμία ανάμειξη με αυτή την ομάδα και δεν ξέρω πώς είμαι σε αυτό, ήμουν ίσως εισάγεται από τρίτα μέρη, δηλώνω ότι είμαι πρόθυμος να συνεργαστεί με την έρευνα και είμαι πρόθυμος να μου να εισαγάγει τη μαρτυρία εάν είναι απαραίτητο, Δηλώνω ότι είμαι εντελώς αθώος και δεν έχουν καμία ανάμειξη με την υπόθεση αυτή δεν εμφανίζεται σε αυτή τη συγκεκριμένη θέση.',
    'في حالة تحقيق الشرطة، أعلن رسميا أن ليس لدي أي مشاركة مع هذه المجموعة، ولا أعرف كيف وانا في ذلك، وأنا ربما كانت تدرج من قبل أطراف ثالثة، أن تعلن وأنا على استعداد للتعاون مع لجنة التحقيق وأنا على استعداد ليعرفني',
    'Em caso de investigação policial, eu oficialmente declaro que não tenho envolvimento com este grupo e não sei como estou no mesmo, provavelmente fui inserido por terceiros, declaro que estou disposto a colaborar com as investigações e estou disposto a me apresentar a depoimento se necessário, declaro que sou completamente inocente e não tenho envolvimento nenhum com este caso mostrado neste post específico.'
]

textosAdmCorno = [
    'Respeite por favor a autoridade... Se vc nao respeitar eh ban.',
    'Ou, fodas',
    '... Vou fingir que não te ouvi....',
    'Você não pode falar isso. Toma ban. @Mafios#5614 da ban nesse corno',
    ':man_police_officer:Por favor, respeite a autoridade... Se vc não respeitar eh ban.:man_police_officer:',
    'O QUE VOCE DISSE? O ADM? CORNO? ESTÁS LOUCO? (deixa ele saber nao kakakak, ele eh cornão)',
    'O QUE VOCE DISSE? O ADM? CORNO? ESTÁS LOUCO? (deixa ele saber nao kakakak, ele eh cornão)'
]


def getEcdiText():
    opcao = random.randint(0, len(textosEmCasoDe))
    return textosEmCasoDe[opcao]


def getEcdText():
    return textosEmCasoDe[0]


def getAdmCornoText():
    opcao = random.randint(0, len(textosAdmCorno))
    return textosAdmCorno[opcao]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!emcasode') or message.content == '!ecd':
        await message.channel.send(getEcdText())
    if message.content == '!ecdi':
        await message.channel.send(getEcdiText())
    if message.content.startswith('!admcorno'):
        await message.channel.send(getAdmCornoText())
    if message.content.startswith('!help'):
        await message.channel.send("""
```
!emcasode ou !ecd - chama o texto que deve ser usado se a call ta meio SUS
!ecdi             - mesma coisa que o de cima, so que pro mundo todo ficar sabendo
!admcorno         - n sei nao, testa ai
```
        """)


client.run(os.getenv('TOKEN'))
