import "package:flutter/material.dart";
import "package:flutter_svg/flutter_svg.dart";

const String assetName = 'assets/cards/01_of_clubs_01.svg';
final Widget svg = SvgPicture.asset(assetName, semanticsLabel: 'Acme Logo');

SvgPicture getCardSvg(String loc, String name) {
  return SvgPicture.asset(loc, semanticsLabel: name);
}

List<SvgPicture> getCardsSvg() {
  List<SvgPicture> cards = <SvgPicture>[];

  List<String> suits = ["CLUB", "DIAMOND", "HEART", "SPADE"];
  List<String> ranks = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11-JACK",
    "12-QUEEN",
    "13-KING"
  ];
  List<String> rankNames = [
    "ACE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE",
    "TEN",
    "JACK",
    "QUEEN",
    "KING"
  ];

  for (String suit in suits) {
    for (int i = 0; i < ranks.length; i++) {
      String name = "${rankNames[i]}_of_${suit}S";
      String loc = "cards/$suit-${ranks[i]}.svg";
      cards.add(getCardSvg(loc, name));
    }
  }

  return cards;
}

class Cards extends StatefulWidget {
  const Cards({Key? key}) : super(key: key);

  @override
  // ignore: library_private_types_in_public_api
  _CardsState createState() => _CardsState();
}

class _CardsState extends State<Cards> {
  final cards = getCardsSvg();
  final cardsOnScreen = <Widget>[];

  int index = 0;

  void spawnCard() {
    debugPrint("spawnCard");
    // cardsOnScreen.add((cards.toList()..shuffle()).first);
    // cardsOnScreen.add(cards.first);

    if (cardsOnScreen.isEmpty) {
      cardsOnScreen.add(cards.first);
    }

    // cardsOnScreen[0] = (cards.toList()..shuffle()).first;
    cardsOnScreen[0] = (cards[index]);
    index++;
    index = index % 52;
    debugPrint("$cardsOnScreen");
  }

  @override
  Widget build(BuildContext context) {
    TextButton addButton = TextButton(
      onPressed: () {
        setState(() {
          spawnCard();
        });
      },
      child: const Text("Spawn card"),
    );
    TextButton clearButton = TextButton(
      onPressed: () {
        setState(() {
          cardsOnScreen.clear();
        });
      },
      child: const Text("Clear cards"),
    );
    return Container(
      alignment: Alignment.center,
      color: const Color.fromARGB(255, 1, 4, 38),
      child: Column(children: cardsOnScreen + [addButton, clearButton]),
    );
  }
}
