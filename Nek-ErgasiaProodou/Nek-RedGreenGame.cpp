                #include <iostream>
                #include <vector>
                #include <cstdlib>
                #include <ctime>
                #include <thread>
                #include <chrono>// afta ta epsaxa gi an ametraei se seconds
                #include <string> //gia to getline
                // den tin ekana elnika den thimame ti thelate giati edo den epzan kai fovithika n ata allaxo
                using namespace std;
                void showStartMenu() {
                    std::cout << "==============================" << std::endl;
                    std::cout << "     RED LIGHT, GREEN LIGHT  " << std::endl;
                    std::cout << "==============================" << std::endl;
                    std::cout << " Press ENTER to start..." << std::endl;
                    std::string input;
                    std::getline(std::cin, input); // enter-den pezei tipota apo grafika kai sas ekana afto
                }
                struct NPC {
                    int id;
                    int position;
                    bool alive;
                    bool finished;
                };
                const int NPC_COUNT = 50;
                const int GOAL = 20;
                const int MAX_SECONDS = 50;// to evala 50 secs eppidi ithel na mpori kapios na ftasei sto finish prin den epizouse kanensas
                const int LIGHT_CHANGE = 3;
                const int RISK = 2;
                bool green = true;
                void toggleLight() {
                    green = !green;
                    cout << (green ? "\n>>> GREEN LIGHT" : "\n>>> RED LIGHT") << endl;
                }
                void playGame() {
                    srand(time(0));
                    vector<NPC> npcs; // lista me tous npc
                    for (int i = 0; i < NPC_COUNT; ++i)
                        npcs.push_back({i + 1, 0, true, false});
                    int seconds = 0;
                    int lightTimer = 0;
                    toggleLight();
                    while (seconds < MAX_SECONDS) {// mexri na teliosei o xronos tha sinexizoun
                        this_thread::sleep_for(chrono::seconds(1));// to epsaxa gia na allazi mono tou tous girous analoga me to xrono 1second
                        seconds++;
                        lightTimer++;
                        cout << "Time: " << seconds << "s" << endl;
                        if (lightTimer == LIGHT_CHANGE) {// kai edo to kommati me psaximo gia ta fos apo kokino se prasino
                            toggleLight();
                            lightTimer = 0;
                        }
                        for (auto& npc : npcs) {
                            if (!npc.alive || npc.finished) continue;
                            if (green) {
                                npc.position++;
                                if (npc.position >= GOAL)
                                    npc.finished = true;
                            } else {
                                if (rand() % 100 < RISK) { //pithanotites
                                    npc.alive = false;
                                    cout << "NPC " << npc.id << " moved on RED LIGHT and was eliminated!" << endl;// fenontai parallila ta apotelesmata
                                }
                            }
                        }
                    }
                    for (auto& npc : npcs) {
                        if (npc.alive && !npc.finished)
                            npc.alive = false;
                    }
                    int finished = 0;
                    for (auto& npc : npcs) {
                        if (npc.finished) finished++;
                    }
                    cout << "\n=== GAME OVER ===" << endl;//apotelesmta
                    int dead = NPC_COUNT - finished;
                    cout << "Finished: " << finished << " | Dead: " << dead << endl;
                    cout << "New total of players: " << finished << endl;
                }
                int main() {
                    showStartMenu();
                    char choice;
                    do {
                        playGame();
                        cout << "\nRestart? (yes/no): ";
                        cin >> choice;
                    } while (choice == 'y' || choice == 'Y');
                    cout << "\n!Thank you for playing!\n";
                    return 0;
                }
