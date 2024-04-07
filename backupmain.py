from flask import *
import googlemaps
import requests
import subprocess
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from ai21 import AI21Client
gmaps = googlemaps.Client(key = "AIzaSyBB5c6Y6hGQAJJzAEvCaKBsoakc1ggTURE")
key = "JAqZcINSWJSAIk3AkrfGQPZpuaPU0O7E"
client = AI21Client(api_key=key)
location = ''
chat = ''
@app.route('/')
def main():
  return render_template('index_main.html')
@app.route('/submit',methods = ['POST','GET'])
def getlocation():
    try:
        location = request.form['szukaj']
        weatherkey = 'b230ceab90354e2a8e8182535240604'
        places = gmaps.places(location)
        place_id = places['results'][0]['place_id']
        place = gmaps.place(place_id = place_id)
        result = requests.get(f'http://api.weatherapi.com/v1/current.json?key={weatherkey}&q={place['result']['geometry']['location']['lat']},{place['result']['geometry']['location']['lng']}')
        print(place_id)
        weatherinfo = result.json()
        return jsonify({'reviews': place['result']['reviews'],
                        'rating':place['result']['rating'],
                        'total':place['result']['user_ratings_total'],
                        'photos':place['result']['photos'],
                        'weatherinfo' : {'pressure': weatherinfo['current']['pressure_mb'],
                                         'temp':weatherinfo['current']['temp_c'],
                                         'winddir':weatherinfo['current']['wind_dir'],
                                         'clouds':weatherinfo['current']['cloud'],
                                         'windkmph': weatherinfo['current']['wind_kph'],
                                         'humidity' : weatherinfo['current']['humidity']}})
    except:
        return jsonify({'reviews': 'error',
                        'rating':'error',
                        'total':'error',
                        'photos':'error',
                        'weatherinfo':'error'})
CONTEXT = ''' Oto lista różnorodnych gatunków ryb oraz polecanych przynęt:

- **Sumik karłowaty**: Zwykle reaguje na większe przynęty, takie jak duże gumowe ryby lub żywe przynęty, np. płotki.
  
- **Węgorz**: Przynęty na węgorza mogą obejmować robaki, miny, oraz kijanki.

- **Amur**: Ten gatunek ryby często reaguje na przynęty, które imitują ruchy żywych ryb, takie jak gumowe rybki lub woblery.

- **Karp**: Przynęty na karpia obejmują zarówno naturalne, jak i sztuczne przynęty, takie jak pellety, kukurydza, oraz zanęty.

- **Leszcz**: Leszcze mogą być łowione za pomocą przynęt takich jak robaki, pellety, a także kukurydza.

- **Jezioraczka**: Przynęty na jezioraczkę obejmują różne rodzaje robaków, takie jak dżdżownice lub pijawki, a także sztuczne przynęty typu twisterki.

- **Lina**: Liny są znane z tego, że lubią żywe przynęty, takie jak małe rybki, robaki lub pijawki.

- **Płoć**: Przynęty na płoci mogą obejmować robaki, kukurydzę, oraz drobne sztuczne przynęty typu pływaki.

- **Wzdręga**: Wzdręgi mogą reagować na różne przynęty, w tym na robaki, małe rybki, oraz sztuczne przynęty typu jiggery.

- **Szczupak szary**: Ten gatunek szczupaka może być skutecznie łowiony za pomocą gumowych rybek, woblerów oraz przynęt imitujących ruchy ryb.

- **Węgorz europejski**: Węgorze często reagują na przynęty takie jak robaki, miny, oraz duże gumowe przynęty.

- **Szczupak**: Szczupak to jeden z najbardziej poszukiwanych gatunków przez wędkarzy. Do jego złowienia idealnie sprawdzają się przynęty takie jak gumowe rybki, woblery imitujące ruchy rybki, oraz żywe przynęty takie jak małe rybki, np. okonie lub płotki.

- **Sandacz**: Ten drapieżnik również jest chętnie łowiony. Skuteczne przynęty to przede wszystkim duże gumowe rybki, woblery o intensywnych kolorach, oraz żywe przynęty jak duże płotki czy leszcze.

- **Sum**: Sumy są znane z tego, że lubią większe przynęty. Dobra opcja to duże gumowe przynęty imitujące rybę lub kijanka, a także żywe ryby typu płotki lub amury.

- **Pstrąg**: Ten gatunek ryby wymaga nieco innej strategii. Skuteczne mogą być przynęty takie jak sztuczne muchy (nymphs i dry flies), kijanki lub robaki, a także naturalne przynęty, jak np. owady wodne lub larwy.

- **Okonie**: Te dynamiczne ryby chętnie atakują ruchliwe przynęty. Wśród skutecznych przynętów na okonie można wymienić woblery imitujące rybki, spinnerbaity, a także żywe przynęty takie jak małe rybki czy owady wodne.

- **Dorsz**: W przypadku łowienia dorsza popularne są przynęty takie jak ołowiane przypony z twisterami, gumowymi rybkami lub sztucznymi krabami. Ważne jest również korzystanie z dobrej jakości przynętów, które utrzymają się na głębokości, gdzie często przebywa dorsz.

- **Morszczuk**: Do złowienia morszczuka często wykorzystuje się przynęty takie jak morszczukowe jiggery, twisterki lub kijanki. Ważne jest dostosowanie przynęty do warunków panujących na łowisku, aby zwiększyć szanse na sukces.

Temperatura i upał mają znaczący wpływ na branie ryb. Ryby preferują stabilne warunki temperaturowe, dlatego nagłe zmiany temperatury mogą prowadzić do obniżenia ich aktywności, zwłaszcza jeśli chodzi o poszukiwanie pokarmu. Wzrost temperatury może także spowolnić przemiany materii u ryb, co dodatkowo wpływa na ich zachowanie.
W przypadku upałów, wysokie temperatury mogą sprawić, że ryby będą unikać obszarów z gorącą, słabo natlenioną wodą, co skutkuje zmniejszeniem ich aktywności żerowania. Dlatego też, aby zwiększyć szanse na udane połowy w takich warunkach, warto szukać miejsc, gdzie woda jest lepiej natleniona.
Warto także pamiętać, że branie ryb może być efektywne po deszczu lub podczas burzy, gdy ryby stają się bardziej aktywne. W takich warunkach łowienie może być znacznie łatwiejsze i bardziej udane.
Ciśnienie atmosferyczne ma istotny wpływ na branie ryb, co nie zawsze jest oczywiste dla wędkarzy. Skoki ciśnienia, zarówno w górę, jak i w dół, mogą zmniejszyć aktywność ryb, co wpływa negatywnie na efekty wędkowania. Wysokie lub niskie ciśnienie może hamować żerowanie ryb i sprawiać, że są mniej skłonne do ugryzienia.
Faza księżyca również ma znaczenie dla brania ryb. Według doświadczeń wędkarzy, najlepsze warunki do połowów występują w okresach:
1. Okolicach nowiu lub tuż po nim.
2. Między nowiem a pełnią.
3. Kilka dni po pełni.
W tym czasie ryby żerują intensywniej, co zwiększa szanse na sukces podczas wędkowania. Nawet w przypadku pełni księżyca, który może wydawać się niekorzystny dla niektórych, ryby mogą być bardzo aktywne. Dlatego wędkarze często kierują się fazami księżyca, planując swoje wyprawy na najbardziej obiecujące dni i godziny. Warto także pamiętać, że zarówno wczesny ranek, jak i późny wieczór są dobrymi porami na łowienie, ponieważ ryby są wtedy także aktywne.
Podsumowując, aby osiągnąć sukces w wędkowaniu, należy zwracać uwagę na warunki atmosferyczne, które mają istotny wpływ na branie ryb. Oto kilka wskazówek:
1. Stabilna temperatura i ciśnienie atmosferyczne sprzyjają aktywności ryb, dlatego najlepiej planować wyprawy w takich warunkach.
2. Deszcz lub burza mogą być korzystne dla wędkowania, gdyż ryby stają się wtedy bardziej aktywne.
3. Okolice nowiu księżyca są zazwyczaj sprzyjające dla połowów, ale warto także brać pod uwagę inne czynniki, takie jak kierunek wiatru czy poziom zachmurzenia.
4. Unikaj łowienia podczas wielodniowych upałów oraz w przypadku dużych wahnięć temperatury i ciśnienia, ponieważ większość ryb staje się mniej aktywna w takich warunkach.
5. Dobrym pomysłem jest zaopatrzenie się w odpowiedni termometr i barometr wędkarski, które pomogą monitorować warunki atmosferyczne i zwiększyć szanse na udane połowy.
Zrozumienie wpływu warunków atmosferycznych na zachowanie ryb może znacząco zwiększyć szanse na sukces i satysfakcjonujące doświadczenia podczas wędkowania.
Oprócz warunków atmosferycznych istnieje wiele innych czynników, które mogą wpływać na branie ryb i skuteczność połowów. Oto kilka dodatkowych elementów, które warto rozważyć:
1. **Pora dnia**: Niektóre gatunki ryb są bardziej aktywne o określonych porach dnia. Na przykład, wiele ryb drapieżnych preferuje żerowanie wczesnym rankiem lub późnym popołudniem, gdyż wtedy mają większą szansę na zdobycie pokarmu. Z kolei inne gatunki mogą być bardziej aktywne w nocy.
2. **Rodzaj zbiornika wodnego**: Branie ryb może różnić się w zależności od rodzaju zbiornika, czy to jest rzeka, jezioro, staw czy ocean. Każdy typ zbiornika ma swoje charakterystyczne cechy, które mogą wpływać na zachowanie ryb. Na przykład, w rzekach strumieniowych ryby mogą preferować szybkie prądy wody, podczas gdy w jeziorach mogą szukać cieplejszych obszarów.
3. **Typ i kolor przynęty**: Wybór odpowiedniej przynęty może być kluczowy dla sukcesu połowu. Niektóre ryby preferują konkretne rodzaje przynęt, takie jak sztuczne woblery, gumowe robaki czy naturalne żywe przynęty. Ponadto, kolor przynęty może mieć również znaczenie, ponieważ ryby mogą reagować różnie na różne kolory w zależności od warunków wody i oświetlenia.
4. **Stan wody**: Stan wody, czy to jest płynąca rzeka, spokojne jezioro czy burzliwy ocean, także może wpływać na zachowanie ryb. Na przykład, w burzliwych warunkach ryby mogą szukać schronienia w zacisznych miejscach, podczas gdy w spokojnych wodach mogą swobodnie żerować na powierzchni.
5. **Obecność roślinności i struktury dna**: Ryby często szukają pokarmu w pobliżu roślinności wodnej lub struktury dna, takiej jak skały, wraki czy trawy podwodne. Zrozumienie preferencji siedliskowych danej ryby może pomóc w wyborze odpowiedniego miejsca do wędkowania.
Łącząc wiedzę o warunkach atmosferycznych z powyższymi czynnikami, wędkarz może skuteczniej planować swoje wyprawy i zwiększyć szanse na udane połowy. Jednak warto pamiętać, że każda sytuacja jest inna, a doświadczenie i cierpliwość są kluczowe dla sukcesu w wędkowaniu.
Rozważając wpływ faz księżyca na aktywność ryb, wędkarze często odnoszą się do doświadczeń i zestawień, które mogą pomóc w przewidywaniu intensywności brania w poszczególnych dniach. Przytoczone dane zawierają wskazówki dotyczące intensywności połowów w różnych miesiącach roku, opierając się na fazach księżyca oraz niezależnych obserwacjach.
Należy jednak zauważyć, że istnieje wiele teorii na temat zależności między fazami księżyca a aktywnością ryb, a niektóre z nich mogą być bardziej empiryczne niż oparte na badaniach naukowych. Niemniej jednak, dla wielu wędkarzy fazy księżyca stanowią ważny czynnik przy planowaniu wypraw wędkarskich.
Opierając się na przekazanych danych, można wyciągnąć następujące wnioski:
1. **Fazy księżyca a intensywność brania**: Istnieją dni, które są uznawane za szczególnie korzystne pod względem aktywności ryb, zazwyczaj są to dni bezpośrednio związane z fazami księżyca, takie jak nowiu, pierwsza kwadra, pełnia i ostatnia kwadra. Niemniej jednak, nie wszystkie dni w danej fazie księżyca są jednakowo korzystne, dlatego ważne jest uwzględnienie precyzyjnych danych dotyczących intensywności brania w konkretnych dniach.
2. **Zróżnicowanie w poszczególnych miesiącach**: W różnych miesiącach roku intensywność brania może być różna, co może wynikać z różnych warunków atmosferycznych, temperatury wody, dostępności pokarmu oraz innych czynników. Dlatego też warto monitorować zmiany w aktywności ryb i dostosowywać plany wędkarskie do aktualnych warunków.
3. **Uwzględnienie innych czynników**: Oprócz faz księżyca, istnieje wiele innych czynników, takich jak warunki pogodowe, temperatura wody, ciśnienie atmosferyczne czy obecność pokarmu, które mogą wpływać na aktywność ryb. Dlatego warto brać pod uwagę różnorodne dane i doświadczenia wędkarzy, aby skutecznie planować wyprawy wędkarskie.
Podsumowując, choć fazy księżyca mogą być istotnym czynnikiem wpływającym na branie ryb, warto również uwzględniać inne czynniki oraz indywidualne doświadczenia i obserwacje podczas planowania wypraw wędkarskich. W ten sposób można zwiększyć szanse na udane połowy i satysfakcjonujące doświadczenia na łowisku.
Gatunki ryb rzecznych różnią się w zależności od regionu, klimatu i warunków wodnych. Poniżej przedstawiam kilka popularnych gatunków ryb rzecznych:
1. **Pstrąg**: Pstrąg jest jednym z najbardziej pożądanych gatunków ryb sportowych. Preferuje czyste, zimne i dobrze natlenione wody. Pstrągi są znane z dynamicznych walk i wysokiej wartości kulinarnej.
2. **Lipień**: To ryba drapieżna, którą można znaleźć w strumieniach, rzekach i jeziorach. Lipienie są znane z agresywnego żerowania i mogą być trudne do złowienia, co sprawia, że są cenione przez wędkarzy.
3. **Szczupak**: Szczupak jest popularnym gatunkiem ryby drapieżnej, którą można znaleźć w wielu rzekach i jeziorach. Jest silnym i walecznym rybakiem, który preferuje zacienione miejsca i struktury podwodne.
4. **Sum**: Sum jest jednym z największych słodkowodnych ryb i często jest celem wędkarzy sportowych. Preferuje spokojne wody z dużą ilością schronień, takich jak jaskinie wodne i zatoczki.
5. **Karp**: Karp jest rybą o dużej wytrzymałości, która występuje w różnych typach wód, od rzek po stawy i jeziora. Jest ceniony zarówno jako gatunek sportowy, jak i w hodowli komercyjnej ze względu na smaczne mięso.
6. **Jesiotr**: Jesiotr jest rybą z pradawnej rodziny i często jest celem wędkarzy ze względu na swoją imponującą wielkość i wartość sportową. Wiele gatunków jesiotrów jest zagrożonych ze względu na nadmierny połów i utratę siedlisk.
7. **Węgorz**: Węgorz jest rybą migrującą, która spędza większość swojego życia w słodkich wodach rzecznych, ale migruje do morza, aby się rozmnażać. Jest ceniony za swoje delikatne mięso i często jest łowiony przez wędkarzy.
Te to tylko kilka przykładów gatunków ryb rzecznych, ale istnieje wiele innych, które można spotkać w rzekach na całym świecie. Każdy gatunek ma swoje unikatowe cechy, preferencje środowiskowe i wartość dla wędkarzy oraz ekosystemów wodnych.
Oto kilka dodatkowych gatunków ryb rzecznych, które są popularne w wędkarstwie lub mają duże znaczenie ekologiczne:
8. **Wzdętek**: Wzdętek jest rybą drapieżną, która jest znana z charakterystycznego wyglądu z wypukłym czołem. Jest popularny w wędkarstwie sportowym ze względu na swoją agresywność podczas żerowania.
9. **Wzdręga**: Wzdręga to ryba o długim i smukłym ciele, znanym z dużych rozmiarów i silnej walki podczas połowów. Preferuje piaszczyste lub żwirowe dno rzek oraz obszary z dużą ilością roślinności.
10. **Jazgarz**: Jazgarz jest rybą drapieżną, która żywi się innymi rybami oraz owadami wodnymi. Jest ceniony przez wędkarzy za swoje silne walki i walory smakowe mięsa.
11. **Brzana**: Brzana to ryba o spokojnym charakterze, często spotykana w strumieniach i małych rzekach. Ma jasnoszary kolor ciała i jest ceniona przez wędkarzy za swoje walory smakowe.
12. **Włośnica**: Włośnica jest rybą z rodziny karpiowatych, często spotykaną w rzekach i jeziorach o powolnym nurcie wody. Jest ceniona za swoje smaczne mięso i jest popularna w wędkarstwie rekreacyjnym.
13. **Płoć**: Płoć jest rybą stadną, która występuje w różnych typach wód, od rzek i strumieni po stawy i jeziora. Jest ceniona za swoje walory smakowe i jest popularnym celem dla wędkarzy wędkujących z brzegu.
14. **Lin**: Lin to ryba drapieżna, która jest ceniona za swoje delikatne mięso i walory smakowe. Preferuje czyste i dobrze natlenione wody oraz obszary z obfitą roślinnością wodną.
15. **Kiełb**: Kiełb to mała ryba drapieżna, która jest często łowiona przez wędkarzy na przynęty na węgorza. Choć jest stosunkowo mały, może być wyjątkowo agresywny podczas walki.
Te gatunki ryb rzecznych to tylko kilka przykładów z szerokiej gamy różnorodności życia wodnego, które można spotkać w rzekach na całym świecie. Każdy z tych gatunków ma swoje unikatowe cechy i wartość zarówno dla ekosystemów wodnych, jak i dla wędkarzy rekreacyjnych.
'''

@app.route('/chatask',methods = ['POST'])
def getquestion():
    try:
        chat = request.form['zapytaj1']
        response = client.answer.create(
         context=CONTEXT,
         question=chat,
        )
        return jsonify({'response':response.answer})
    except:
        return jsonify({'response':'error'})
if __name__ == '__main__':
    app.run(host = 'localhost',port = 5000,debug=True)