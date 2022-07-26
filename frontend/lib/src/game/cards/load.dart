import "package:flutter_svg/flutter_svg.dart";
import "package:collection/collection.dart";

const List<String> suits = ["CLUB", "DIAMOND", "HEART", "SPADE"];
const List<String> ranks = [
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
const List<String> rankNames = [
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

SvgPicture getCardSvg(String loc, String name,
    {double? height, double? width}) {
  return SvgPicture.asset(
    loc,
    semanticsLabel: name,
    height: height,
    width: width,
  );
}

///
/// Do not specify height or width to get default values.
/// If height is specified, width will be calculated from it.
/// If width is specified, height will be calculated from it.
/// If both are specified, width will be calculated from height.
///
List<SvgPicture> getCardsSvg({double? height, double? width}) {
  List<SvgPicture> cards = <SvgPicture>[];

  for (String suit in suits) {
    // for (int i = 0; i < ranks.length; i++) {
    //   String name = "${rankNames[i]}_of_${suit}S";
    //   String loc = "cards/$suit-${ranks[i]}.svg";

    //   var cardSvg = getCardSvg(loc, name, height: height, width: width);
    //   cards.add(cardSvg);
    // }
    for (final pair in IterableZip([ranks, rankNames])) {
      final rank = pair[0];
      final rankName = pair[1];

      String loc = "cards/$suit-$rank.svg";
      String name = "${rankName}_of_${suit}S";

      var cardSvg = getCardSvg(loc, name, height: height, width: width);
      cards.add(cardSvg);
    }
  }

  return cards;
}
