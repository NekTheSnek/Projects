// edo einai mesa oti exei na kanei me to ui kommati
//den mporousa na to trexo xoris ta libraries edo...
//fanatzome giati einai gia to swing ui kai t alip
import javax.swing.*;
import java.awt.*;
// einai i sindesi gia to main arxio kai enimeroni gneika ti main
public class Frame {
    private final Main controller;
    JFrame frame;
    JTextArea textArea;
    JButton[] btn = new JButton[7]; // epiloges
    JButton restartBtn;//alalgi stis epiloges dld otan alazei to kimeno
    CardLayout cards;
    JPanel root;
    //edo aplaonomsa ta parathora
    final String PAGE_MENU = "menu";
    final String PAGE_GAME = "game";
    private ImageIcon bookIcon;
    private JLabel bookBg;
    private final int MENU_W = 460;//diastais ta vrika ligo skoura edo
    private final int MENU_H = 680;//gia to proto parathiro
    private final double GAME_SCALE = 1.10;//gia to deftero
    private int GAME_W;
    private int GAME_H;
    private Font storyFont  = new Font("Serif", Font.PLAIN, 16);
    private Font optionFont = new Font("Serif", Font.PLAIN, 14);
    private Color normalColor = new Color(40, 30, 20);
    private Color hoverColor  = new Color(120, 70, 10);
    private Timer typingTimer;
    private int typingIndex = 0;//afta einai gia to typing efect gia tous xaraktires
    public Frame(Main controller) {
        this.controller = controller;
        //dimiourgia tou protou parathirou
        //genika edo eixa ena thema me to kentrasrism akai genika em tis ikones
        //opote epese ligo psaximo epese poli vasika
        frame = new JFrame("The King in Yellow");
        frame.setIconImage(new ImageIcon("imgs/sign.png").getImage());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        bookIcon = new ImageIcon("imgs/book.png");
        if (bookIcon.getIconWidth() > 0) {
            GAME_W = (int)(bookIcon.getIconWidth() * GAME_SCALE);
            GAME_H = (int)(bookIcon.getIconHeight() * GAME_SCALE);
        } else {
            GAME_W = 1100;
            GAME_H = 600;
        }
        cards = new CardLayout();
        root = new JPanel(cards);
        root.add(buildMenuPage(), PAGE_MENU);
        root.add(buildGamePage(), PAGE_GAME);
        frame.setContentPane(root);
        frame.setLocationRelativeTo(null);
        frame.setSize(MENU_W, MENU_H);
        frame.setVisible(true);

        showMenu();
    }
    private void setGameSizeExact() {
        Insets in = frame.getInsets();
        frame.setSize(GAME_W + in.left + in.right, GAME_H + in.top + in.bottom);
        frame.setLocationRelativeTo(null);
    }
    //gia to menu dldl tin proti se ldia
    JPanel buildMenuPage() {
        JPanel menu = new JPanel(new GridBagLayout());

        JLabel title = new JLabel("The King in Yellow");
        title.setFont(new Font("Serif", Font.BOLD, 34));

        ImageIcon coverIcon = new ImageIcon("imgs/king.png");
        Image img = coverIcon.getImage().getScaledInstance(300, 410, Image.SCALE_SMOOTH);
        JLabel coverLabel = new JLabel(new ImageIcon(img));

        JButton startBtn = new JButton("Begin Adventure");
        startBtn.setFont(new Font("Serif", Font.BOLD, 17));
        startBtn.setPreferredSize(new Dimension(215, 52));
        startBtn.setFocusPainted(false);

        startBtn.addActionListener(e -> {
            showGame();
            setGameSizeExact();
            controller.StartGame();
        });
        //edo erixa geli poli den epiane me tpota
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(12, 10, 16, 10);
        menu.add(title, gbc);
        gbc.gridy = 1;
        gbc.insets = new Insets(0, 10, 14, 10);
        menu.add(coverLabel, gbc);
        gbc.gridy = 2;
        gbc.insets = new Insets(12, 10, 10, 10);
        menu.add(startBtn, gbc);

        return menu;
    }
    //edo irthe kai me estile anagastika na xoriso tis selides giati den engene me tipota omorfo
    //vgenane ola mazi tora einai aristera kai dexia omrfa kai orea
    JPanel buildGamePage() {
        JPanel game = new JPanel(new BorderLayout());

        Image scaledBook = bookIcon.getImage().getScaledInstance(GAME_W, GAME_H, Image.SCALE_SMOOTH);
        bookBg = new JLabel(new ImageIcon(scaledBook));
        bookBg.setLayout(new BorderLayout());

        JPanel pages = new JPanel(new GridLayout(1, 2));
        pages.setOpaque(false);
        textArea = new JTextArea();
        textArea.setEditable(false);
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        textArea.setFont(storyFont);
        textArea.setForeground(normalColor);
        textArea.setOpaque(false);
        textArea.setMargin(new Insets(80, 120, 70, 70));

        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setBorder(BorderFactory.createEmptyBorder());
        scrollPane.setOpaque(false);
        scrollPane.getViewport().setOpaque(false);
        scrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER);

        JPanel optionsPanel = new JPanel(new GridLayout(8, 1, 0, 14));
        optionsPanel.setOpaque(false);
        optionsPanel.setBorder(BorderFactory.createEmptyBorder(90, 30, 70, 40));
        for (int i = 0; i < 7; i++) {
            final int idx = i;
            final int choice = i + 1;

            btn[i] = new JButton();
            btn[i].setFont(optionFont);
            btn[i].setForeground(normalColor);
            btn[i].setOpaque(false);
            btn[i].setContentAreaFilled(false);
            btn[i].setBorderPainted(false);
            btn[i].setFocusPainted(false);
            btn[i].setHorizontalAlignment(SwingConstants.LEFT);
            btn[i].addMouseListener(new java.awt.event.MouseAdapter() {
                @Override
                public void mouseEntered(java.awt.event.MouseEvent e) {
                    if (!btn[idx].isEnabled()) return;
                    btn[idx].setForeground(hoverColor);
                    btn[idx].setCursor(new Cursor(Cursor.HAND_CURSOR));
                }
                @Override
                public void mouseExited(java.awt.event.MouseEvent e) {
                    btn[idx].setForeground(normalColor);
                    btn[idx].setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
                }
            });
            btn[i].addActionListener(e -> controller.handleChoice(choice));
            optionsPanel.add(btn[i]);
        }

        restartBtn = new JButton("Restart");
        restartBtn.setFont(new Font("Serif", Font.BOLD, 16));
        restartBtn.setForeground(normalColor);
        restartBtn.setOpaque(false);
        restartBtn.setContentAreaFilled(false);
        restartBtn.setBorderPainted(false);
        restartBtn.setFocusPainted(false);
        restartBtn.setHorizontalAlignment(SwingConstants.LEFT);//
        //hooverrr
        restartBtn.addMouseListener(new java.awt.event.MouseAdapter() {
            @Override
            public void mouseEntered(java.awt.event.MouseEvent e) {
                if (!restartBtn.isEnabled()) return;
                restartBtn.setForeground(hoverColor);
                restartBtn.setCursor(new Cursor(Cursor.HAND_CURSOR));
            }

            @Override
            public void mouseExited(java.awt.event.MouseEvent e) {
                restartBtn.setForeground(normalColor);
                restartBtn.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
            }
        });
        // episis den katafera na valo timousiki exo afisi to arxio mesa omos
        restartBtn.setEnabled(true);
        restartBtn.addActionListener(e -> controller.StartGame());
        optionsPanel.add(restartBtn);
        pages.add(scrollPane);
        pages.add(optionsPanel);
        bookBg.add(pages, BorderLayout.CENTER);
        game.add(bookBg, BorderLayout.CENTER);

        return game;
    }

    public void showMenu() { cards.show(root, PAGE_MENU); }
    public void showGame() { cards.show(root, PAGE_GAME); }

    public void setText(String text) {
        stopTyping();
        textArea.setText(text);
        textArea.setCaretPosition(0);
    }

    public void setTextTyping(String text, int delayMs) {
        stopTyping();

        enableChoices(false);
        if (restartBtn != null) restartBtn.setEnabled(true);

        textArea.setText("");
        typingIndex = 0;

        typingTimer = new Timer(delayMs, e -> {
            if (typingIndex < text.length()) {
                textArea.append(String.valueOf(text.charAt(typingIndex)));
                typingIndex++;
                textArea.setCaretPosition(textArea.getDocument().getLength());
            } else {
                ((Timer) e.getSource()).stop();
                textArea.setCaretPosition(0);

                enableChoices(true);
                if (restartBtn != null) restartBtn.setEnabled(true);
            }
        });

        typingTimer.start();
    }

    private void stopTyping() {
        if (typingTimer != null && typingTimer.isRunning()) typingTimer.stop();
    }
    public void setButtons(String[] options) {
        for (int i = 0; i < 7; i++) {
            if (options != null && i < options.length) {
                btn[i].setText((i + 1) + ". " + options[i]);
                btn[i].setVisible(true);
                btn[i].setEnabled(true);
            } else {
                btn[i].setText("");
                btn[i].setVisible(false);
                btn[i].setEnabled(false);
            }

            if (btn[i] != null) btn[i].setForeground(normalColor);
        }
        if (restartBtn != null) {
            restartBtn.setForeground(normalColor);
            restartBtn.setEnabled(true);
        }

        frame.revalidate();
        frame.repaint();
    }
    public void enableChoices(boolean enabled) {
        for (JButton b : btn) {
            if (b != null && b.isVisible()) b.setEnabled(enabled);
        }
    }
}

