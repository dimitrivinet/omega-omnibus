import "package:flutter/material.dart";
import "package:flutter_svg/flutter_svg.dart";
import 'package:frontend/src/game/cards/play.dart';
import "dart:math";
import "load.dart";

// typical card is 2.5" x 3.5" (64x89mm)
const double cardAspectRatio = 64.0 / 89.0;
const double cardHeight = 150.0;
const double cardWidth = cardHeight * cardAspectRatio;

const double playAreaWidth = 800.0;
const double playAreaHeight = 800.0;

class Cards extends StatefulWidget {
  const Cards({Key? key}) : super(key: key);

  @override
  // ignore: library_private_types_in_public_api
  _CardsState createState() => _CardsState();
}

class _CardsState extends State<Cards> {
  final cards = getCardsSvg(height: cardHeight);
  final cardsOnScreen = <Widget>[];
  final cardThumbsOnScreen = <SvgPicture>[];
  final maxCards = 12;
  var disableSpawning = false;
  Random rng = Random();

  int index = 0;

  void spawnCard() {
    debugPrint("spawnCard");

    // cardsOnScreen.add((cards.toList()..shuffle()).first);
    // OR
    var randCard = (cards.toList()..shuffle()).first;

    cardsOnScreen.add(
      // Positioned(
      //   bottom: rng.nextDouble() *
      //       (playAreaHeight - cardHeight), // random y position
      //   right: rng.nextDouble() * (playAreaWidth - cardWidth),
      //   child: randCard,
      // ),
      PlayedCard(
        playAreaHeight: playAreaHeight,
        cardHeight: cardHeight,
        playAreaWidth: playAreaWidth,
        cardWidth: cardWidth,
        child: randCard,
      ),
    );

    cardThumbsOnScreen.add(randCard);
    // OR
    // cardsOnScreen.add(cards.first);
    // OR
    // if (cardsOnScreen.isEmpty) {
    //   cardsOnScreen.add(cards.first);
    // }
    // cardsOnScreen[0] = (cards.toList()..shuffle()).first;
    // OR
    // if (cardsOnScreen.isEmpty) {
    //   cardsOnScreen.add(cards.first);
    // }
    // cardsOnScreen[0] = (cards[index]);
    // index++;
    // index = index % 52;

    if (cardsOnScreen.length >= maxCards) {
      disableSpawning = true;
    }

    debugPrint("$cardsOnScreen");
    debugPrint("$cardThumbsOnScreen");
  }

  @override
  Widget build(BuildContext context) {
    var playArea = Container(
      color: Colors.blue,
      child: SizedBox(
          height: playAreaHeight,
          width: playAreaWidth,
          child: Stack(
            children: cardsOnScreen,
          )),
    );

    var addButton = TextButton(
      onPressed: disableSpawning
          ? null
          : () {
              setState(() {
                spawnCard();
              });
            },
      child: const Text("Spawn card"),
    );

    var clearButton = TextButton(
      onPressed: () {
        setState(() {
          cardsOnScreen.clear();
          cardThumbsOnScreen.clear();
          disableSpawning = false;
        });
      },
      child: const Text("Clear cards"),
    );

    var thumbGrid = SizedBox(
      height: playAreaHeight,
      width: playAreaWidth / 2,
      child: GridView.builder(
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 3,
          childAspectRatio: 0.7,
          mainAxisSpacing: 10,
          crossAxisSpacing: 10,
        ),
        itemCount: cardThumbsOnScreen.length,
        itemBuilder: (BuildContext ctx, index) {
          return cardThumbsOnScreen[index];
        },
      ),
    );

    return Container(
      alignment: Alignment.center,
      color: const Color.fromARGB(255, 1, 4, 38),
      child: Container(
        margin: const EdgeInsets.only(top: 10),
        decoration:
            BoxDecoration(border: Border.all(width: 2, color: Colors.white)),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Column(children: [playArea, addButton, clearButton]),
            const SizedBox(width: 10),
            thumbGrid,
          ],
        ),
      ),
    );
  }
}
