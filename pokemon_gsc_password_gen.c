#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* --- Data structure for player info --- */
typedef struct {
    char name[8];      /* max 7 characters + null */
    int trainer_id;
    int money;
} Player;

/* --- Function: Convert character to numeric value --- */
int char_to_value(char c) {
    switch(c) {
        case 'A': return 128; case 'B': return 129; case 'C': return 130;
        case 'D': return 131; case 'E': return 132; case 'F': return 133;
        case 'G': return 134; case 'H': return 135; case 'I': return 136;
        case 'J': return 137; case 'K': return 138; case 'L': return 139;
        case 'M': return 140; case 'N': return 141; case 'O': return 142;
        case 'P': return 143; case 'Q': return 144; case 'R': return 145;
        case 'S': return 146; case 'T': return 147; case 'U': return 148;
        case 'V': return 149; case 'W': return 150; case 'X': return 151;
        case 'Y': return 152; case 'Z': return 153;
        case '(': return 154; case ')': return 155; case ':': return 156;
        case ';': return 157; case '[': return 158; case ']': return 159;
        case 'a': return 160; case 'b': return 161; case 'c': return 162;
        case 'd': return 163; case 'e': return 164; case 'f': return 165;
        case 'g': return 166; case 'h': return 167; case 'i': return 168;
        case 'j': return 169; case 'k': return 170; case 'l': return 171;
        case 'm': return 172; case 'n': return 173; case 'o': return 174;
        case 'p': return 175; case 'q': return 176; case 'r': return 177;
        case 's': return 178; case 't': return 179; case 'u': return 180;
        case 'v': return 181; case 'w': return 182; case 'x': return 183;
        case 'y': return 184; case 'z': return 185;
        case '{': return 225; case '}': return 226; case '-': return 227;
        case '?': return 230; case '!': return 231; case '.': return 232;
        case '*': return 241; case '/': return 243; case ',': return 244;
        case ' ': return 0;
        default: return -1; /* invalid character */
    }
}

/* --- Function: Compute name total --- */
int compute_name_total(const char *name) {
    int total = 0;
    int i, val;
    for (i = 0; i < 5 && name[i] != '\0'; i++) {
        val = char_to_value(name[i]);
        if (val == -1) {
            fprintf(stderr, "ER004: Name contains invalid character.\n");
            exit(1);
        }
        total += val;
    }
    if (i < 5) total += 80;
    return total;
}

/* --- Function: Compute money total --- */
int compute_money_total(int money) {
    int byte1 = money / 65536;
    int byte2 = (money / 256) % 256;
    int byte3 = money % 256;
    return byte1 + byte2 + byte3;
}

/* --- Function: Compute trainer ID total --- */
int compute_trainer_total(int trainer_id) {
    int byte1 = trainer_id / 256;
    int byte2 = trainer_id % 256;
    return byte1 + byte2;
}

/* --- Function: Generate password --- */
int generate_password(const Player *p) {
    int name_total = compute_name_total(p->name);
    int money_total = compute_money_total(p->money);
    int trainer_total = compute_trainer_total(p->trainer_id);
    return name_total + money_total + trainer_total;
}

/* --- Function: Read player input --- */
void read_player(Player *p) {
    printf("Enter name of player character (use { for PK and } for MN):\n> ");
    if (scanf("%7s", p->name) != 1) {
        fprintf(stderr, "ER005: Name must not be blank.\n");
        exit(1);
    }
    if (strlen(p->name) > 7) {
        fprintf(stderr, "ER001: Name must be only 7 characters long.\n");
        exit(1);
    }

    printf("Enter ID number:\n> ");
    if (scanf("%d", &p->trainer_id) != 1) {
        fprintf(stderr, "ER006: Trainer ID must be a number.\n");
        exit(1);
    }
    if (!(0 <= p->trainer_id && p->trainer_id <= 65535)) {
        fprintf(stderr, "ER002: Trainer ID must be from 00000 to 65536.\n");
        exit(1);
    }

    printf("Enter amount of held money:\n> ");
    if (scanf("%d", &p->money) != 1) {
        fprintf(stderr, "ER007: Amount of money must be a number.\n");
        exit(1);
    }
    if (!(0 <= p->money && p->money <= 999999)) {
        fprintf(stderr, "ER003: Amount of money must be 0-999999.\n");
        exit(1);
    }
}

/* --- Main --- */
int main(void) {
    Player player;
    int password;

    read_player(&player);
    password = generate_password(&player);

    printf("\n%s/%05d, %d units of currency\n",
           player.name, player.trainer_id, player.money);
    printf("Password: %05d\n", password);

    return 0;
}
