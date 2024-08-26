
import images # type: ignore
import strings #type:ignore
bids = {}
newBidder = True

def init():
    print(images.gavel)

def clearScreen():
    print("\n" * 100)

def getBid():
    bidder = input(f"{strings.askForName}\n")
    bid = input(f"{strings.askForBid}\n")
    bids[bidder] = int(bid)

def showWinner():
    winningBid = 0
    winningBidder = ""
    for bidder in bids:
        if(bids[bidder] > winningBid):
            winningBid = bids[bidder]
            winningBidder = bidder
    print(f"{strings.announceWinningBid}{winningBid}, {strings.announceWinningBidder} {winningBidder}")

init()
while newBidder:
    getBid()
    closeAuction = input(f"{strings.checkForNewBidder}\n").lower()
    clearScreen()
    if closeAuction != "yes":
        newBidder = False
        showWinner()