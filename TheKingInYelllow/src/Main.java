public class Main {
    // sindeete me to frame.
    Frame ui;
    //
    final int START = 0;
    final int SEARCH_THE_ROOM = 1;
    final int SEARCH_FOR_EXIT = 2;
    final int INVESTIGATE_OBJECT = 3;
    final int DESCEND_STAIRCASE = 4;
    final int INSPECT_SYMBOL = 5;
    final int MEET_THE_KING = 6;
    final int EXAMINE_SYMBOLS = 7;
    final int MEDITATE = 8;
    final int FOLLOW_WHISPERS = 9;
    final int CALL_FOR_HELP = 10;
    final int PICKUP_BOOK = 11;
    final int CLOSE_EYES = 12;
    final int END = 99;

    int scene = START;
    // lipon afto to evala mono kai mono gia to auto type efect pou exo valei
    //prospathisa kai em allous tropous alla den ginotane se olo to kimeno mono
    // se simia opote to epsaxa kai tora pezei asxeta apo pia epilogi einai kathe fora
    boolean typingOn = false;
    final int TYPE_DELAY = 50;
// edo kai pera dld mexri na vro to simio pou xekinisa kati allo xekinaei to ui
    //alla epidi den eixame kanei polla ekatsa kai vrika diafora pragmatakia
   // merika einai se sindiasmo me oti exouem di
    public Main() {
        ui = new Frame(this);
        ui.showMenu();//gia to proto parathiro to menu se eisagogika
    }
    void endGame() {
        scene = END;
        ui.enableChoices(false);
    }
    // lipon edo exei mpei kai to boolean apo prin gia na diatitrite se kathe epilogi
    //epiddi xrisimopiounte kai se alla arxia vasika sindeonte ola mazi sinexos
    //ithela na kno pio polla sto ui kommati alla nomizo mexri edo pros to paron
    //ta ipolpa einai polla
    private void showScene(String text, String[] options) {
        if (typingOn) ui.setTextTyping(text, TYPE_DELAY);
        else ui.setText(text);
        ui.setButtons(options);
        ui.enableChoices(true);
    }
    //itan diskolo na ta sindeso ola afta signomi akoam diavazo gia merika
    void handleChoice(int c) {//
        switch (scene) {
            case START:// edo einaii arxi tou typing effect sti  proti epilgi
                //kai gineet enabled kai gia tis ipolipes
                if (c == 1) {
                    typingOn = true;
                    SearchtheRoom();
                }
                else if (c == 2) ExamineSymbols();
                else if (c == 3) FollowWhispers();
                else if (c == 4) CallforHelp();
                else if (c == 5) PickupBook();
                else if (c == 6) Meditate();
                else if (c == 7) CloseEyes();
                break;
            case SEARCH_THE_ROOM:
                if (c == 1) Meditate();
                else if (c == 2) ExamineSymbols();
                else if (c == 3) CloseEyes();
                break;
            case SEARCH_FOR_EXIT:
                if (c == 1) {
                    ui.setText(
                            "You push with all your strength, but the door does not budge.\n" +
                                    "The whispers grow louder, mocking your efforts.\n\n" +
                                    "GAME OVER."
                    );
                    endGame();
                } else if (c == 2) {
                    InvestigateObject();
                }
                break;
            case INVESTIGATE_OBJECT:
                if (c == 1) DescendStaircase();
                else if (c == 2) InspectSymbol();
                break;
            case DESCEND_STAIRCASE:
                if (c == 1) MeettheKing();
                else if (c == 2) InspectSymbol();
                else if (c == 3) {
                    ui.setText(
                            "You manage to go back, but the whispers are now deafening.\n" +
                                    "The door you entered is gone and you are now trapped.\n\n" +
                                    "GAME OVER."
                    );
                    endGame();
                }
                break;
            case INSPECT_SYMBOL:
                if (c == 1) {
                    ui.setText(
                            "A searing pain floods your mind as you touch the symbols.\n" +
                                    "You see visions of a dark city under a pale sun.\n\n" +
                                    "GAME OVER."
                    );
                    endGame();
                } else if (c == 2) {
                    MeettheKing();
                } else if (c == 3) {
                    ui.setText(
                            "You step away, but the symbols whisper into your mind.\n" +
                                    "The cavern trembles and the whispers are now deafening.\n" +
                                    "Have you seen the Yellow sign?\n\n" +
                                    "GAME OVER."
                    );
                    endGame();
                }
                break;
            case MEET_THE_KING:
                if (c == 1 || c == 2 || c == 3) {
                    ui.setText("The King in Yellow watches.\n\nGAME OVER.");
                    endGame();
                }
                break;
            case EXAMINE_SYMBOLS:
                if (c == 1) {
                    ui.setText(
                            "As you trace the symbols, visions of Carcosa flood your mind.\n\n" +
                                    "GAME OVER."
                    );
                    endGame();
                } else if (c == 2) {
                    SearchforExit();
                } else if (c == 3) {
                    ui.setText("You turn away from the symbols.\n\nGAME OVER.");
                    endGame();
                }
                break;
            case MEDITATE:
                if (c == 1) SearchforExit();
                else if (c == 2) FollowWhispers();
                break;
            case FOLLOW_WHISPERS:
                ui.setText("The whispers consume you.\n\nGAME OVER.");
                endGame();
                break;
            case CALL_FOR_HELP:
                if (c == 1) {
                    ui.setText("The King in Yellow answers.\n\nGAME OVER.");
                    endGame();
                } else if (c == 2) {
                    SearchtheRoom();
                }
                break;
            case PICKUP_BOOK:
                ui.setText("The knowledge binds your mind.\n\nGAME OVER.");
                endGame();
                break;
            case CLOSE_EYES:
                ui.setText("You have seen the Yellow sign.\n\nGAME OVER.");
                endGame();
                break;
            case END:
                break;
        }
    }
    void StartGame() {
        scene = START;
        showScene(Story.START_TEXT, Story.START_OPTIONS);
    }
    void SearchtheRoom() {
        scene = SEARCH_THE_ROOM;
        showScene(Story.SEARCH_THE_ROOM_TEXT, Story.SEARCH_THE_ROOM_OPTIONS);
    }
    void SearchforExit() {
        scene = SEARCH_FOR_EXIT;
        showScene(Story.SEARCH_FOR_EXIT_TEXT, Story.SEARCH_FOR_EXIT_OPTIONS);
    }
    void InvestigateObject() {
        scene = INVESTIGATE_OBJECT;
        showScene(Story.INVESTIGATE_OBJECT_TEXT, Story.INVESTIGATE_OBJECT_OPTIONS);
    }
    void DescendStaircase() {
        scene = DESCEND_STAIRCASE;
        showScene(Story.DESCEND_STAIRCASE_TEXT, Story.DESCEND_STAIRCASE_OPTIONS);
    }
    void InspectSymbol() {
        scene = INSPECT_SYMBOL;
        showScene(Story.INSPECT_SYMBOL_TEXT, Story.INSPECT_SYMBOL_OPTIONS);
    }
    void MeettheKing() {
        scene = MEET_THE_KING;
        showScene(Story.MEET_THE_KING_TEXT, Story.MEET_THE_KING_OPTIONS);
    }
    void ExamineSymbols() {
        scene = EXAMINE_SYMBOLS;
        showScene(Story.EXAMINE_SYMBOLS_TEXT, Story.EXAMINE_SYMBOLS_OPTIONS);
    }
    void Meditate() {
        scene = MEDITATE;
        showScene(Story.MEDITATE_TEXT, Story.MEDITATE_OPTIONS);
    }
    void FollowWhispers() {
        scene = FOLLOW_WHISPERS;
        showScene(Story.FOLLOW_WHISPERS_TEXT, Story.FOLLOW_WHISPERS_OPTIONS);
    }
    void CallforHelp() {
        scene = CALL_FOR_HELP;
        showScene(Story.CALL_FOR_HELP_TEXT, Story.CALL_FOR_HELP_OPTIONS);
    }
    void PickupBook() {
        scene = PICKUP_BOOK;
        showScene(Story.PICKUP_BOOK_TEXT, Story.PICKUP_BOOK_OPTIONS);
    }
    void CloseEyes() {
        scene = CLOSE_EYES;
        showScene(Story.CLOSE_EYES_TEXT, Story.CLOSE_EYES_OPTIONS);
    }
    public static void main(String[] args) {
        new Main();
    }
}

