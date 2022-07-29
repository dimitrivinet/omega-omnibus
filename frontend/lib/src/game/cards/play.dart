import "dart:math";
import "package:flutter/material.dart";

Random rng = Random();
const cardSources = <Offset>[
  Offset(-2, -2),
  Offset(2, -2),
  Offset(2, 2),
  Offset(-2, 2),
];
var cardSourceIndex = -1;

class PlayedCard extends StatefulWidget {
  // final double playAreaHeight;
  // final double playAreaWidth;
  final double cardHeight;
  final double cardWidth;
  final Widget child;

  const PlayedCard(
      {
      // required this.playAreaHeight,
      required this.cardHeight,
      // required this.playAreaWidth,
      required this.cardWidth,
      required this.child,
      Key? key})
      : super(key: key);

  @override
  State<PlayedCard> createState() => _PlayedCardState();
}

class _PlayedCardState extends State<PlayedCard>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller = AnimationController(
    duration: const Duration(milliseconds: 700),
    vsync: this,
  )
    // ..repeat(reverse: true)
    ..forward();

  late final Animation<Offset> _offsetAnimation = Tween<Offset>(
    begin: cardSources[cardSourceIndex],
    end: Offset.zero,
  ).animate(CurvedAnimation(
    parent: _controller,
    curve: Curves.easeOut,
  ));

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    cardSourceIndex = (cardSourceIndex + 1) % cardSources.length;

    // var bottomRange = widget.playAreaHeight - widget.cardHeight;
    // var rightRange = widget.playAreaWidth - widget.cardWidth;

    // var bottomPos = rng.nextDouble() * bottomRange / 2 + (bottomRange / 4);
    // var rightPos = rng.nextDouble() * rightRange / 2 + (rightRange / 4);
    var bottomPos = rng.nextDouble() * 2 - 1;
    var rightPos = rng.nextDouble() * 2 - 1;
    // var bottomPos = 0.5;
    // var rightPos = 0.5;

    return Align(
      alignment: Alignment(bottomPos, rightPos),
      child: SlideTransition(
        position: _offsetAnimation,
        child: widget.child,
      ),
    );
  }
}
