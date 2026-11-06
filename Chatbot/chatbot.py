import tkinter as tk # arxi tis tkinter 
from tkinter import simpledialog, messagebox # gia ta parathira kai isagogi minimaton
import re # gia ta gramata kai ton elexno tous otan grafei o user
from datetime import datetime # gia imerominia dimiourgias sto istoriko apothikvsis 
#po po o kodikas mou einai xalia signomi alla einai opos ta evaza otan diavaza oti skeftomoun empene apo kato 

#rithimisis parathirou
title = "Dino Bot"
size = "680x520"   
t = 40  # pio argo typing gia to bot
bg = "#0b0f1a" 
chat_bg  = "#0f1629"  
panel = "#111c44"  
text_fg  = "#e6f1ff"   
b_send  = "#00eaff"   
b_learn = "#ff2fd2"   
b_clear = "#8a2be2"  
btn_font = ("Arial", 12)
chat_font = ("Arial", 13) 

history = "chat_history.txt"   #arxio istorikou sinomilas
memory = "learn_memory.txt"   # arxio mnimis learn 
#edo pira voithia gia an to stiso ligo kalitera
closing = False
# save/istoriko
def save_to_history(line):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # afto to pira epidi mouto evgale san extra mazi me ti voithia gia to save histroy 
    #kai apla to afisa :P einai gia na vazi stamps imeromina stin apothikefsi
    f = open(history, "a", encoding="utf-8")
    f.write("[" + timestamp + "] " + line + "\n")
    f.close()
#save kenourgia sinomilia sto istriko nea sinomilia
def new_session():
    save_to_history("======================================")
    save_to_history("NEW SESSION")
    save_to_history("======================================")
# clear history
def clear_history_file():
    f = open(history, "w", encoding="utf-8")
    f.write("")
    f.close()
# save gia to learn
def save_memory(keyword, answer):
    f = open(memory, "a", encoding="utf-8")
    f.write(keyword + "||" + answer + "\n")
    f.close()
# diavazi ta apothikevmena sto learn etsi oste na ta thimate stin epomeni sinomilia
def load_memory():
    # Διαβάζει το learn_memory.txt 
    try:
        f = open(memory, "r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "||" in line:
                key, value = line.split("||", 1)
                key = key.strip()
                value = value.strip()
                if key:
                    knowledge[key] = value
        f.close()
    except:
        pass
# ekana ta idi apothikevmena etsi epidi logo tou greeklish den apothikevontan allios me tipota kai to kitaxa
# ta emoji eno to exo vali utf 8 gia kapio logo den fenonte kanonika...den to epsaxa poli na po tin alithia to afia etsi 
knowledge = {
    "hello": "Ροαρρ! 🦖 Γεια σου!",
    "hi": "Ροαρρ! 🦖 Τι κάνεις;",
    "how are you": "Ροαρρ! 😄 Είμαι σούπερ! Εσύ;",
    "name": "Ροαρρ! 🦖 Με λένε Ναμίρα! Είμαι ένα cyber Dino Bot! 💙",

    "γεια": "Ροαρρ! 🦖 Γεια σου!",
    "καλησπερα": "Ροαρρ! 🌙 Καλησπέρα!",
    "τι κανεις": "Ροαρρ! 😄 Είμαι τέλεια! Μαθαίνω και παίζω!",
    "ονομα": "Ροαρρ! 🦖 Με λένε Ναμίρα! Cyber Dino Bot 💙",

    "τι ειναι python": "Ροαρρ! 🦖 Η Python είναι γλώσσα προγραμματισμού.",
    "τι ειναι list": "Ροαρρ! 📋 Η list κρατά πολλές τιμές μέσα σε μία λίστα.",
    "τι ειναι tuple": "Ροαρρ! 🔒 Το tuple μοιάζει με list αλλά δεν αλλάζει.",
    "τι ειναι if": "Ροαρρ! ✅ Η if ελέγχει συνθήκες (αν ισχύει κάτι).",
    "τι ειναι for": "Ροαρρ! 🔁 Η for κάνει επανάληψη (loop).",
    "τι ειναι while": "Ροαρρ! ⏳ Η while επαναλαμβάνει όσο ισχύει μια συνθήκη.",
    "τι ειναι function": "Ροαρρ! 🧩 Η function είναι κομμάτι κώδικα που κάνει μια δουλειά.",
    "τι ειναι variable": "Ροαρρ! 📦 Η variable αποθηκεύει τιμές.",
    "τι ειναι string": "Ροαρρ! ✍️ Το string είναι κείμενο.",
    "τι ειναι integer": "Ροαρρ! 🔢 Το integer είναι ακέραιος αριθμός."
}
# metvlites gia to learn sti glossa
unknown = None
unknown_lang = "gr"
# lipon afto den doulevi opos tha ithela ithela na diavazi oti kai na grapsi o xristis
# alla den mou evgene me tipota kai tora apla mpori na diavazi afta ta dilomena kai na apothikevi kanonika sto learn kai se greeklish
#afto tha apantaei sta ellinika
greek = str.maketrans({
    "ά": "α", "έ": "ε", "ή": "η", "ί": "ι", "ό": "ο", "ύ": "υ", "ώ": "ω",
    "ϊ": "ι", "ΐ": "ι", "ϋ": "υ", "ΰ": "υ",
    "Ά": "α", "Έ": "ε", "Ή": "η", "Ί": "ι", "Ό": "ο", "Ύ": "υ", "Ώ": "ω"
})
greeklish = str.maketrans({
    "a": "α", "b": "β", "v": "β", "g": "γ", "d": "δ", "e": "ε", "z": "ζ",
    "h": "η", "i": "ι", "k": "κ", "l": "λ", "m": "μ", "n": "ν",
    "o": "ο", "p": "π", "r": "ρ", "s": "σ", "t": "τ", "u": "ου",
    "f": "φ", "x": "χ", "y": "υ", "w": "ω", "q": "κ", "j": "τζ"
})
# edo irthe i megaliteri voithia kai to simio pou to exsa afto pou ipa prin kai to afisa opos einai
# aferei tonous kai megala mikra garammata etsi oste na mpori na diavasi polles parallages 
def strip_tonos(s):
    return s.translate(greek)
# extra replacements glossas 
def greeklish_to_greek(s):
    s = s.lower()
    s = (s.replace("th", "θ")
           .replace("ch", "χ")
           .replace("x", "χ")
           .replace("h", "χ")
           .replace("ps", "ψ")
           .replace("ks", "ξ")
           .replace("x", "ξ")
           .replace("g", "γκ")
           .replace("ou", "ου")
           .replace("ai", "αι")
           .replace("e", "αι")
           .replace("ei", "ει")
           .replace("i", "ει")
           .replace("oi", "οι")
           .replace("i", "οι"))
    return s.translate(greeklish)

def normalize(text):
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    msg1 = strip_tonos(text)
    gr = greeklish_to_greek(text)
    msg2 = strip_tonos(gr)
    return msg1, msg2

def has_greek_letters(s):
    return re.search(r"[α-ωΑ-Ω]", s) is not None
# dimiourgia parathirou GUI
def window_setup():
    global closing
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    window.configure(bg=bg)
# mou exafanizontan ta koumpia otan ekana pano stis rithimisis allages sto size kai afto vithise na to krataei stahero to megthos 
# edo kati exo kani periergo tha exogiso sti sinexia tou kdika sto scrollbar
    window.minsize(680, 520)
 # klini to parathiro
    def on_close():
        global closing
        closing = True
        window.destroy()
    window.protocol("WM_DELETE_WINDOW", on_close)
     # gia fortosi tou ico tou paarthirou
    try:
        window.iconbitmap("dino.ico")
    except:
        print("Δεν βρέθηκε το icon")
    label = tk.Label(
        window,
        text="Dino Bot",
        font=("Arial", 18, "bold"),
        bg=bg,
        fg=text_fg
    )
    label.pack(pady=8)
 # buttons, kai o xoros tou type gia to user
    bottom = tk.Frame(window, bg=bg)
    bottom.pack(side="bottom", fill="x", pady=8)
    frame = tk.Frame(bottom, bg=bg)
    frame.pack(side="bottom")
    entry = tk.Entry(
        bottom,
        font=("Arial", 12),
        bg=panel,
        fg=text_fg,
        relief="flat",
        insertbackground=b_send
    )
    entry.pack(side="bottom", padx=10, pady=8, fill="x")
    entry.insert(0, "Type here")
  # chat  meros gia emfansi sinomilas + scrollabar
    chat_frame = tk.Frame(window, bg=bg)
    chat_frame.pack(padx=10, pady=8, fill="both", expand=True)
  # lipon to scrollbar doulevei kanonika alla den fenete me tis rithimisis parathirou pou exo valei 
  #fenete mono an to valoume full screen 
  #kati exei na kanei me to fix pou evala prin gi ato parathiro alal o kodikas mou vgike megalos kai eixa xathei ligo gia na to kitaxo pio poli 
  #signomiiii alla doulevei ta xromata pu eixa valei den emfanizonte
    scrollbar = tk.Scrollbar(
        chat_frame,
        orient="vertical",
        width=14,
        bg=b_send,
        troughcolor=chat_bg,
        activebackground=b_learn,
        highlightbackground=b_send,
        highlightcolor=b_send,
        bd=0,
        relief="flat"
    )
    chat = tk.Text(
        chat_frame,
        state="disabled",
        font=chat_font,  
        bg=chat_bg,
        fg=text_fg,
        relief="flat",
        yscrollcommand=scrollbar.set,
        insertbackground=b_send
    )
    scrollbar.config(command=chat.yview)
    chat.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    return window, chat, entry, frame
# print gia to chat 
def user_print(chat, text):
    chat.config(state="normal")
    chat.insert("end", "You: " + text + "\n")
    chat.config(state="disabled")
    chat.see("end")
    save_to_history("You: " + text)
# gia to bot genika me slow typing
def bot_print(window, chat, text):
    global closing
    if closing:
        return
    try:
        if not window.winfo_exists() or not chat.winfo_exists():
            return
    except tk.TclError:
        return
    try:
        chat.config(state="normal")
        chat.insert("end", "Namira: ")
        for ch in text:
            if closing:
                return
            try:
                if not window.winfo_exists() or not chat.winfo_exists():
                    return
            except tk.TclError:
                return
            chat.insert("end", ch)
            chat.update()
            chat.after(t)
        chat.insert("end", "\n")
        chat.config(state="disabled")
        chat.see("end")
        save_to_history("Namira: " + text)
    except tk.TclError:
        return
# i main function 
def main():
    global unknown, unknown_lang
    window, chat, entry, frame = window_setup() # dimiourgia parathirou
    load_memory() 
    new_session()
   # gia to send 
    def send():
        global unknown, unknown_lang
        raw = entry.get()
        entry.delete(0, "end")
        if not raw.strip():
            return
        # minima bot gia keno minima 
        user_print(chat, raw)
        msg1, msg2 = normalize(raw)
        if msg1 in knowledge:
            bot_print(window, chat, knowledge[msg1])
            unknown = None
            return
        if msg2 in knowledge:
            bot_print(window, chat, knowledge[msg2])
            unknown = None
            return
        # minima bot an the xeri na apantisisi
        bot_print(window, chat, "Ουπς! 🦖😅 Δεν το ξέρω αυτό ακόμα! Πάτα Learn να μου το μάθεις!")
        if has_greek_letters(raw):
            unknown = msg2
            unknown_lang = "gr"
        else:
            unknown = msg1
            unknown_lang = "gl"
    # minimata bot pros to user gia to learn kai tin apothilevsi + ti tha grafi otan patisi o user to learn kai anixei to allo parathiro
    def learn():
        global unknown, unknown_lang
        if unknown is None:
            messagebox.showinfo("Learn", "Ροαρρ! 🦖 Δεν υπάρχει άγνωστη ερώτηση τώρα 🙂")
            return
        if unknown_lang == "gl":
            answer = simpledialog.askstring(
                "Learn",
                "🧠 Dino Learn Mode!\nTi apantisi na dinw gia:\n'" + unknown + "'"
            )
        else:
            answer = simpledialog.askstring(
                "Learn",
                "🧠 Λειτουργία Μάθησης (Dino Mode)!\nΤι απάντηση να δίνω για:\n'" + unknown + "'"
            )
        if not answer:
            return
        # meta tin apothikevsi sto learn kai save sto history 
        knowledge[unknown] = answer
        save_memory(unknown, answer)
        save_to_history("----- LEARN -----")
        save_to_history("Keyword: " + unknown)
        save_to_history("Answer: " + answer)
        save_to_history("-----------------")
        bot_print(window, chat, "Ροαρρ! 🦖💙 Το έμαθα! Έγινα πιο έξυπνη τώρα 😄")
        unknown = None
   # clear history ektos apoto learn kai minimata tou bot erotisi apothikevsis kai epiveveosi clear
    def clear_all():
        ok = messagebox.askyesno("Clear", "Ροαρρ! 🦖 Να διαγραφεί όλο το ιστορικό συνομιλίας;")
        if not ok:
            return
        clear_history_file()
        chat.config(state="normal")
        chat.delete("1.0", "end")
        chat.config(state="disabled")
        bot_print(window, chat, "Ροαρρ! 🧹 Όλα καθαρά! Το ιστορικό μηδενίστηκε 😅")
    # buttons parathirou
    tk.Button(
        frame, text="Send", width=12, command=send,
        bg=b_send, fg="black", activeforeground="black",
        relief="flat", font=btn_font
    ).pack(side="left", padx=10)
    tk.Button(
        frame, text="Learn", width=12, command=learn,
        bg=b_learn, fg="black", activeforeground="black",
        relief="flat", font=btn_font
    ).pack(side="left", padx=10)
    tk.Button(
        frame, text="Clear", width=12, command=clear_all,
        bg=b_clear, fg="black", activeforeground="black",
        relief="flat", font=btn_font
    ).pack(side="left", padx=10)
    window.bind("<Return>", lambda e: send())
    # arxiko minima bot /kalosorisma sti sinomilia
    bot_print(window, chat, "Ροαρρ! 🦖⚡ Είμαι η Ναμίρα, ένα Dino bot...!!!! Γράψε κάτι να ξεκινήσουμε 😄")
    window.mainloop()
# telos terastio vgike kai den to xo teliosi kanonika 
if __name__ == "__main__":
    main()