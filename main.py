# ============================================================
# KUZRAT - CLASS 10 SCIENCE PREMIUM STUDY APP
# Password: KUZRAT10
# Chapters: 1-14
# Practice Sets: 1-10
# Each Paper: 80 Marks | 3 Hours 15 Minutes
# ============================================================

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


# ------------------------------------------------------------
# PREMIUM COLORS
# ------------------------------------------------------------

BG = (0.025, 0.035, 0.07, 1)
PANEL = (0.055, 0.07, 0.12, 1)
CARD = (0.075, 0.095, 0.16, 1)
GOLD = (1.0, 0.72, 0.18, 1)
GOLD2 = (0.85, 0.55, 0.08, 1)
BLUE = (0.12, 0.42, 0.95, 1)
PURPLE = (0.45, 0.22, 0.85, 1)
GREEN = (0.12, 0.68, 0.38, 1)
RED = (0.9, 0.2, 0.25, 1)
WHITE = (0.96, 0.98, 1, 1)
MUTED = (0.65, 0.72, 0.82, 1)


# ------------------------------------------------------------
# CHAPTERS
# ------------------------------------------------------------

CHAPTERS = [
    ("01", "Chemical Reactions and Equations"),
    ("02", "Acids, Bases and Salts"),
    ("03", "Metals and Non-metals"),
    ("04", "Carbon and Its Compounds"),
    ("05", "Life Processes"),
    ("06", "Control and Coordination"),
    ("07", "How Do Organisms Reproduce?"),
    ("08", "Heredity"),
    ("09", "Our Environment"),
    ("10", "Light – Reflection and Refraction"),
    ("11", "The Human Eye and the Colourful World"),
    ("12", "Electricity"),
    ("13", "Magnetic Effects of Electric Current"),
    ("14", "Sources of Energy"),
]


# ------------------------------------------------------------
# DEEP NOTES
# ------------------------------------------------------------

NOTES = {

"01": """
CHEMICAL REACTIONS AND EQUATIONS

1. Chemical Reaction
A chemical reaction is a process in which one or more substances
change into new substances having different properties.

Signs of a chemical reaction:
• Change in colour
• Change in temperature
• Evolution of gas
• Formation of precipitate
• Change in state

2. Chemical Equation
A chemical equation represents a chemical reaction using symbols
and formulae.

Example:
Mg + O2 → MgO

Balanced equation:
2Mg + O2 → 2MgO

3. Law of Conservation of Mass
Mass can neither be created nor destroyed in a chemical reaction.
Therefore the number of atoms of every element must be equal on
both sides of a balanced equation.

4. Types of Chemical Reactions

Combination:
Two or more substances combine to form one product.

CaO + H2O → Ca(OH)2

Decomposition:
One compound breaks into simpler substances.

CaCO3 → CaO + CO2

Displacement:
A more reactive element displaces a less reactive element.

Zn + CuSO4 → ZnSO4 + Cu

Double Displacement:
Exchange of ions takes place.

Na2SO4 + BaCl2 → BaSO4 + 2NaCl

5. Oxidation
Addition of oxygen or removal of hydrogen is oxidation.

2Cu + O2 → 2CuO

6. Reduction
Removal of oxygen or addition of hydrogen is reduction.

CuO + H2 → Cu + H2O

7. Redox Reaction
Oxidation and reduction occur simultaneously.

8. Corrosion
Slow destruction of metals by reaction with air, moisture or
chemicals.

Rusting of iron produces hydrated iron oxide.

9. Rancidity
Oxidation of fats and oils causes unpleasant smell and taste.

Prevention:
• Refrigeration
• Antioxidants
• Airtight packing
• Nitrogen flushing

IMPORTANT EQUATIONS

2Mg + O2 → 2MgO
Zn + CuSO4 → ZnSO4 + Cu
CaCO3 → CaO + CO2
2AgCl → 2Ag + Cl2
CuO + H2 → Cu + H2O
""",

"02": """
ACIDS, BASES AND SALTS

1. Acids
Acids produce H+ ions in aqueous solution.

Examples:
HCl, H2SO4, HNO3

2. Bases
Bases produce OH- ions in aqueous solution.

Examples:
NaOH, KOH, Ca(OH)2

3. Indicators

Litmus:
Acid → blue litmus becomes red
Base → red litmus becomes blue

Phenolphthalein:
Acid → colourless
Base → pink

Methyl orange:
Acid → red
Base → yellow

4. pH Scale

pH range = 0 to 14

pH < 7 → acidic
pH = 7 → neutral
pH > 7 → basic

Lower pH means stronger acidity.

5. Acid + Metal

Acid + Metal → Salt + Hydrogen

Zn + 2HCl → ZnCl2 + H2

6. Acid + Base

Acid + Base → Salt + Water

HCl + NaOH → NaCl + H2O

This is neutralisation.

7. Acid + Carbonate

Acid + Carbonate → Salt + Water + CO2

Na2CO3 + 2HCl → 2NaCl + H2O + CO2

8. Common Salt

NaCl is sodium chloride.

9. Baking Soda

NaHCO3 = sodium hydrogen carbonate.

On heating:

2NaHCO3 → Na2CO3 + H2O + CO2

Uses:
• Baking
• Antacid
• Fire extinguishers

10. Washing Soda

Na2CO3·10H2O

Uses:
• Cleaning
• Removing permanent hardness of water
• Glass, soap and paper industries

11. Bleaching Powder

CaOCl2

Uses:
• Disinfecting drinking water
• Bleaching cotton and paper

12. Plaster of Paris

CaSO4·1/2H2O

On mixing with water it forms gypsum.

13. Chlor-alkali Process

Electrolysis of brine produces:
NaOH + H2 + Cl2

VERY IMPORTANT:
pH = 7 → neutral
HCl + NaOH → NaCl + H2O
""",

"03": """
METALS AND NON-METALS

METALS

Physical properties:
• Lustrous
• Malleable
• Ductile
• Sonorous
• Good conductors
• Generally high melting points

NON-METALS

Usually:
• Brittle
• Dull
• Poor conductors
• Not malleable
• Not ductile

IMPORTANT EXCEPTION:
Graphite conducts electricity.

REACTIVITY SERIES

K > Na > Ca > Mg > Al > Zn > Fe > Pb > H >
Cu > Hg > Ag > Au

A metal higher in the series can displace a metal below it.

Zn + CuSO4 → ZnSO4 + Cu

IONIC COMPOUNDS

Formed by transfer of electrons.

Properties:
• Hard
• High melting points
• High boiling points
• Conduct electricity in molten or aqueous state

EXTRACTION OF METALS

Low reactive metals:
May occur in native state.

Medium reactive metals:
Usually obtained by reduction of oxides.

Highly reactive metals:
Obtained by electrolysis.

CORROSION

Iron + oxygen + water → rust

Prevention:
• Painting
• Oiling
• Greasing
• Galvanisation
• Alloying

ALLOYS

Mixtures of metals or metal + non-metal.

Examples:
Brass = Copper + Zinc
Bronze = Copper + Tin
Steel = Iron + Carbon

IMPORTANT:
Sodium and potassium are stored under kerosene because they
react vigorously with air and water.
""",

"04": """
CARBON AND ITS COMPOUNDS

Carbon has atomic number 6.

VALENCY = 4

Two special properties:

1. Tetravalency
Carbon forms four covalent bonds.

2. Catenation
Carbon atoms can bond with one another to form chains and rings.

COVALENT BOND

Formed by sharing of electrons.

Examples:
CH4
C2H6
C2H4
C2H2

SATURATED COMPOUNDS

Contain only single bonds.

Example:
Ethane C2H6

UNSATURATED COMPOUNDS

Contain double or triple bonds.

Ethene C2H4
Ethyne C2H2

HOMOLOGOUS SERIES

A series of compounds having:
• Same functional group
• Same general formula
• Similar chemical properties
• Consecutive members differ by CH2

FUNCTIONAL GROUPS

Alcohol → –OH
Aldehyde → –CHO
Ketone → >C=O
Carboxylic acid → –COOH
Halogen → –Cl, –Br etc.

ETHANOL

Formula: C2H5OH

Uses:
• Solvent
• Fuel
• Industrial chemical

ETHANOIC ACID

Formula: CH3COOH

Common name: Acetic acid

ESTERIFICATION

Alcohol + Carboxylic acid → Ester + Water

C2H5OH + CH3COOH → Ester + H2O

SAPONIFICATION

Ester + NaOH → Soap + Alcohol

IMPORTANT:
Carbon forms a huge number of compounds because of tetravalency
and catenation.
""",

"05": """
LIFE PROCESSES

Life processes include:
• Nutrition
• Respiration
• Transportation
• Excretion

PHOTOSYNTHESIS

6CO2 + 6H2O → C6H12O6 + 6O2

Conditions:
• Sunlight
• Chlorophyll

NUTRITION

Autotrophic nutrition:
Plants prepare food.

Heterotrophic nutrition:
Organisms obtain food from other organisms.

HUMAN DIGESTIVE SYSTEM

Mouth → Oesophagus → Stomach → Small intestine →
Large intestine → Rectum → Anus

Small intestine:
Main site of digestion and absorption.

VILLI:
Finger-like projections that increase surface area for absorption.

RESPIRATION

Aerobic:
Glucose + Oxygen → CO2 + H2O + Energy

Anaerobic:
Occurs without oxygen.

TRANSPORTATION

Human circulatory system contains:
• Heart
• Blood
• Blood vessels

Blood components:
RBC → oxygen transport
WBC → defence
Platelets → clotting
Plasma → transport medium

DOUBLE CIRCULATION

Blood passes through the heart twice during one complete cycle.

PLANTS

Xylem → transports water and minerals.

Phloem → transports food.

EXCRETION

Kidneys remove nitrogenous wastes.

NEPHRON:
Structural and functional unit of kidney.

Main processes:
• Filtration
• Reabsorption
• Secretion
""",

"06": """
CONTROL AND COORDINATION

Nervous system controls and coordinates body activities.

NEURON

Basic structural and functional unit of nervous system.

Parts:
• Dendrites
• Cell body
• Axon

REFLEX ACTION

A quick automatic response to a stimulus.

REFLEX ARC:

Receptor → Sensory neuron → Spinal cord →
Motor neuron → Effector

BRAIN

Forebrain:
Thinking, memory, intelligence and sensory interpretation.

Midbrain:
Controls some reflexes.

Hindbrain:
Balance, posture, breathing and heartbeat.

PLANT HORMONES

Auxin → growth
Gibberellin → stem growth
Cytokinin → cell division
Abscisic acid → inhibits growth
Ethylene → fruit ripening

ANIMAL HORMONES

Insulin → controls blood glucose
Adrenaline → emergency response
Thyroxine → metabolism
Growth hormone → growth
""",

"07": """
HOW DO ORGANISMS REPRODUCE?

Reproduction produces new individuals.

ASEXUAL REPRODUCTION

Only one parent.

Methods:
• Fission
• Budding
• Fragmentation
• Regeneration
• Spore formation
• Vegetative propagation

SEXUAL REPRODUCTION

Involves male and female gametes.

MALE REPRODUCTIVE SYSTEM

Main organs:
• Testes
• Vas deferens
• Urethra
• Penis

Testes produce sperm and testosterone.

FEMALE REPRODUCTIVE SYSTEM

Main organs:
• Ovaries
• Oviducts
• Uterus
• Cervix
• Vagina

Fertilisation usually occurs in the fallopian tube/oviduct.

ZYGOTE

Fusion of sperm and egg forms a zygote.

IMPLANTATION

Embryo attaches to the lining of uterus.

PUBERTY

Sex hormones cause physical and reproductive changes.

MENSTRUAL CYCLE

Usually about 28 days, though it varies among individuals.

IMPORTANT:
Fertilisation = fusion of male and female gametes.
""",

"08": """
HEREDITY

Heredity is transmission of traits from parents to offspring.

VARIATION

Differences among individuals of the same species.

GENE

Functional unit of heredity.

DNA

DNA carries genetic information.

CHROMOSOMES

DNA is organised into chromosomes.

MENDEL

Gregor Mendel performed experiments on pea plants.

DOMINANT TRAIT

Expressed even in heterozygous condition.

RECESSIVE TRAIT

Expressed when dominant allele is absent.

MONOHYBRID CROSS

Example:
TT × tt

F1:
All Tt

F2:
Tt × Tt

Phenotypic ratio:
3 Tall : 1 Dwarf

Genotypic ratio:
1 TT : 2 Tt : 1 tt

SEX DETERMINATION

Female → XX
Male → XY

Mother gives X chromosome.

Father gives X or Y.

XX → female child
XY → male child

DIHYBRID CROSS

Typical phenotypic ratio:
9 : 3 : 3 : 1

IMPORTANT:
Genes are located on chromosomes.
""",

"09": """
OUR ENVIRONMENT

ECOSYSTEM

An ecosystem consists of living organisms and their physical
environment.

BIOTIC COMPONENTS:
Plants, animals, microorganisms.

ABIOTIC COMPONENTS:
Air, water, soil, temperature, light.

PRODUCERS

Plants prepare food.

CONSUMERS

Depend directly or indirectly on producers.

DECOMPOSERS

Bacteria and fungi break down dead matter.

FOOD CHAIN

Example:

Grass → Grasshopper → Frog → Snake → Eagle

ENERGY FLOW

Energy flow in an ecosystem is unidirectional.

10% LAW

Only about 10% of energy at one trophic level is transferred to
the next level.

BIODEGRADABLE

Can be broken down naturally by microorganisms.

NON-BIODEGRADABLE

Do not break down easily.

BIOMAGNIFICATION

Concentration of harmful chemicals increases at higher trophic
levels.

OZONE

Ozone layer protects Earth from harmful ultraviolet radiation.

CFCs contribute to ozone depletion.
""",

"10": """
LIGHT – REFLECTION AND REFRACTION

REFLECTION

Bouncing back of light from a surface.

LAWS OF REFLECTION

1. Angle of incidence = angle of reflection.
2. Incident ray, reflected ray and normal lie in same plane.

MIRROR FORMULA

1/f = 1/v + 1/u

MAGNIFICATION

m = -v/u

CONCAVE MIRROR

Can form real or virtual images depending on object position.

Uses:
• Shaving mirrors
• Headlights
• Solar furnaces

CONVEX MIRROR

Always forms virtual, erect and diminished image.

Used as rear-view mirror.

REFRACTION

Bending of light when it travels from one medium to another.

LENS FORMULA

1/f = 1/v - 1/u

LENS MAGNIFICATION

m = v/u

POWER OF LENS

P = 1/f

Here f must be in metres.

Unit = dioptre (D)

Convex lens:
Positive power.

Concave lens:
Negative power.

SIGN CONVENTION IS VERY IMPORTANT IN NUMERICALS.
""",

"11": """
THE HUMAN EYE AND THE COLOURFUL WORLD

HUMAN EYE

Main parts:
• Cornea
• Iris
• Pupil
• Lens
• Retina
• Optic nerve
• Ciliary muscles

ACCOMMODATION

Ability of eye lens to change focal length to focus objects at
different distances.

MYOPIA

Near-sightedness.

Distant objects are not seen clearly.

Correction:
Concave lens.

HYPERMETROPIA

Far-sightedness.

Correction:
Convex lens.

PRESBYOPIA

Age-related loss of accommodation.

May require bifocal/progressive lenses.

DISPERSION

Splitting of white light into colours.

VIBGYOR:
Violet
Indigo
Blue
Green
Yellow
Orange
Red

RAINBOW

Produced due to:
• Refraction
• Dispersion
• Internal reflection

SCATTERING

Shorter wavelengths scatter more strongly.

Blue sky is mainly due to scattering of blue light.

SUNRISE/SUNSET

Sun appears reddish because longer wavelengths reach the eye
more effectively after scattering of shorter wavelengths.
""",

"12": """
ELECTRICITY

ELECTRIC CURRENT

I = Q/t

SI unit = Ampere.

POTENTIAL DIFFERENCE

V = W/Q

SI unit = Volt.

OHM'S LAW

V = IR

Resistance:
R = V/I

RESISTIVITY

R = ρL/A

Series combination:

R = R1 + R2 + R3

Same current flows through all resistors.

Parallel combination:

1/R = 1/R1 + 1/R2 + 1/R3

Same potential difference across each branch.

ELECTRIC POWER

P = VI

Also:

P = I²R
P = V²/R

ELECTRICAL ENERGY

E = Pt

Commercial unit:
1 kWh = 3.6 × 10^6 J

FUSE

A safety device that melts when excessive current flows.

IMPORTANT:
Always use SI units in numerical problems.
""",

"13": """
MAGNETIC EFFECTS OF ELECTRIC CURRENT

A current-carrying conductor produces a magnetic field.

RIGHT-HAND THUMB RULE

If the right thumb points in direction of current, curled fingers
show direction of magnetic field.

SOLENOID

A coil of many circular turns of insulated wire.

It produces a magnetic field similar to a bar magnet.

ELECTRIC MOTOR

Converts:
Electrical energy → Mechanical energy

Main parts:
• Coil
• Magnet
• Split-ring commutator
• Brushes
• Battery

FLEMING'S LEFT-HAND RULE

Used to determine direction of force on a current-carrying
conductor in a magnetic field.

ELECTROMAGNETIC INDUCTION

Production of electric current due to changing magnetic field.

GENERATOR

Converts:
Mechanical energy → Electrical energy

FLEMING'S RIGHT-HAND RULE

Used to determine direction of induced current.

MOTOR vs GENERATOR

Motor:
Electrical → Mechanical

Generator:
Mechanical → Electrical
""",

"14": """
SOURCES OF ENERGY

A good source of energy should:
• Produce large amount of energy
• Be economical
• Be easily available
• Be easy to store and transport
• Cause minimum pollution

RENEWABLE SOURCES

Can be replenished naturally.

Examples:
• Solar
• Wind
• Hydroelectric
• Biomass
• Geothermal

NON-RENEWABLE SOURCES

Limited resources.

Examples:
• Coal
• Petroleum
• Natural gas
• Nuclear fuels

SOLAR ENERGY

Energy from Sun.

Advantages:
• Renewable
• Clean
• Abundant

WIND ENERGY

Uses kinetic energy of moving air.

HYDRO ENERGY

Uses energy of flowing/falling water.

BIOMASS

Organic material used as fuel.

BIOGAS

Main component = methane.

NUCLEAR ENERGY

Released during nuclear reactions.

FISSION:
Heavy nucleus splits into smaller nuclei.

FUSION:
Light nuclei combine to form heavier nucleus.

Fossil fuels cause air pollution and release greenhouse gases.

IMPORTANT:
Renewable sources are naturally replenished.
"""
}


# ------------------------------------------------------------
# QUESTION BANK
# ------------------------------------------------------------

MCQS = [
    ("Which reaction is a displacement reaction?",
     ["Zn + CuSO4 → ZnSO4 + Cu", "HCl + NaOH → NaCl + H2O",
      "CaCO3 → CaO + CO2", "2Mg + O2 → 2MgO"], "A"),

    ("The pH of a neutral solution is:",
     ["0", "7", "14", "5"], "B"),

    ("Which metal is generally stored under kerosene?",
     ["Iron", "Copper", "Sodium", "Silver"], "C"),

    ("The functional group of alcohol is:",
     ["–COOH", "–CHO", "–OH", "–CO–"], "C"),

    ("The structural and functional unit of kidney is:",
     ["Neuron", "Nephron", "Villus", "Alveolus"], "B"),

    ("Auxin mainly promotes:",
     ["Plant growth", "Blood clotting", "Digestion", "Respiration"], "A"),

    ("The genetic material in humans is:",
     ["Protein", "DNA", "Fat", "Glucose"], "B"),

    ("The male sex chromosome combination is:",
     ["XX", "XY", "YY", "XO"], "B"),

    ("Energy flow in an ecosystem is:",
     ["Cyclic", "Random", "Unidirectional", "Reversible"], "C"),

    ("Myopia is corrected using:",
     ["Convex lens", "Concave lens", "Plane mirror", "Cylindrical mirror"], "B"),

    ("SI unit of electric current is:",
     ["Volt", "Ohm", "Ampere", "Watt"], "C"),

    ("Ohm's law is:",
     ["P=VI", "V=IR", "I=Q/t", "E=Pt"], "B"),

    ("1 kWh is equal to:",
     ["3.6×10^6 J", "360 J", "36 J", "3.6×10^3 J"], "A"),

    ("An electric motor converts:",
     ["Mechanical to electrical", "Electrical to mechanical",
      "Heat to light", "Chemical to nuclear"], "B"),

    ("Right-hand thumb rule gives direction of:",
     ["Electric current", "Magnetic field",
      "Gravity", "Light"], "B"),

    ("A generator works on:",
     ["Electrolysis", "Electromagnetic induction",
      "Neutralisation", "Photosynthesis"], "B"),

    ("The major component of biogas is:",
     ["Oxygen", "Nitrogen", "Methane", "Hydrogen"], "C"),

    ("A nuclear reactor commonly uses:",
     ["Nuclear fission", "Nuclear reflection",
      "Chemical decomposition", "Photosynthesis"], "A"),
]


SHORT_QUESTIONS = [
    "Balance Fe + H2O → Fe3O4 + H2 and identify the type of reaction.",
    "What happens when an acid reacts with a metal? Give one equation.",
    "Why do ionic compounds have high melting points?",
    "Differentiate between saturated and unsaturated hydrocarbons.",
    "What are villi? State their function.",
    "What is reflex action? Give one example.",
    "Where does fertilisation usually occur in human females?",
    "Differentiate between dominant and recessive traits.",
    "State the two laws of reflection.",
    "A resistor of 5 Ω carries 2 A current. Find the potential difference.",
    "Write two differences between series and parallel combination.",
    "What is the function of a fuse?"
]


LONG_QUESTIONS = [
    "Explain oxidation, reduction and redox reaction with suitable examples.",
    "Explain double circulation in human beings.",
    "Explain myopia and hypermetropia and their correction.",
    "A resistor of 10 Ω is connected to 20 V. Calculate current and power.",
    "Explain photosynthesis and write its balanced chemical equation.",
    "Explain Mendel's monohybrid cross and obtain the 3:1 phenotypic ratio.",
    "Explain electromagnetic induction and the working principle of a generator.",
    "Explain the extraction of a moderately reactive metal from its ore.",
    "Describe the structure and working of a nephron.",
    "Explain image formation by a concave mirror using the mirror formula."
]


VERY_LONG_QUESTIONS = [
    "Explain the complete human digestive system. Include the role of mouth, stomach, small intestine, villi, large intestine and associated glands.",
    "Explain the structure of the human eye, accommodation, myopia, hypermetropia and their corrections.",
    "Derive the equivalent resistance relations for series and parallel combinations and solve a suitable numerical.",
    "Explain male and female reproductive systems, fertilisation, implantation and the role of reproductive hormones.",
    "Compare renewable and non-renewable sources of energy with advantages, disadvantages and examples.",
    "Explain the construction and working of an electric motor and state Fleming's left-hand rule.",
    "Explain acids and bases, pH scale, neutralisation, baking soda and washing soda with important equations.",
    "Explain carbon's tetravalency and catenation. Describe homologous series, functional groups and esterification."
]


# ------------------------------------------------------------
# PAPER VARIATION
# ------------------------------------------------------------

PAPER_TOPICS = [
    "Chemical Reactions and Equations",
    "Acids, Bases and Salts",
    "Metals and Non-metals",
    "Carbon and Its Compounds",
    "Life Processes",
    "Control and Coordination",
    "Reproduction",
    "Heredity",
    "Our Environment",
    "Light",
    "Human Eye",
    "Electricity",
    "Magnetism",
    "Sources of Energy"
]


def make_paper(number):
    """
    Creates a distinct practice paper by rotating question banks.
    Every paper keeps the same 80-mark structure.
    """

    shift = (number - 1) % len(MCQS)

    mcqs = MCQS[shift:] + MCQS[:shift]

    short_shift = (number - 1) % len(SHORT_QUESTIONS)
    shorts = SHORT_QUESTIONS[short_shift:] + SHORT_QUESTIONS[:short_shift]

    long_shift = (number - 1) % len(LONG_QUESTIONS)
    longs = LONG_QUESTIONS[long_shift:] + LONG_QUESTIONS[:long_shift]

    very_shift = (number - 1) % len(VERY_LONG_QUESTIONS)
    very = VERY_LONG_QUESTIONS[very_shift:] + VERY_LONG_QUESTIONS[:very_shift]

    return {
        "mcqs": mcqs[:18],
        "short": shorts[:12],
        "long": longs[:10],
        "very": very[:8]
    }


PAPERS = {i: make_paper(i) for i in range(1, 11)}


# ------------------------------------------------------------
# COMMON UI HELPERS
# ------------------------------------------------------------

def rounded_background(widget, color=CARD, radius=18):
    with widget.canvas.before:
        Color(*color)
        widget._bg = RoundedRectangle(
            pos=widget.pos,
            size=widget.size,
            radius=[dp(radius)]
        )

    def update_bg(instance, value):
        instance._bg.pos = instance.pos
        instance._bg.size = instance.size

    widget.bind(pos=update_bg, size=update_bg)


class PremiumButton(Button):

    def __init__(self, bg_color=CARD, text_color=WHITE,
                 radius=16, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)
        self.color = text_color
        self.font_size = sp(15)
        self.bold = True

        with self.canvas.before:
            Color(*bg_color)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(radius)]
            )

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class GoldTitle(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = GOLD
        self.bold = True


# ------------------------------------------------------------
# LOGIN SCREEN
# ------------------------------------------------------------

class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=[dp(25), dp(45)],
            spacing=dp(18)
        )

        root.add_widget(Label(
            text="👑",
            font_size=sp(55),
            size_hint_y=None,
            height=dp(70)
        ))

        title = Label(
            text="KUZRAT",
            font_size=sp(36),
            bold=True,
            color=GOLD,
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(title)

        root.add_widget(Label(
            text="CLASS 10 • SCIENCE",
            font_size=sp(16),
            color=WHITE,
            size_hint_y=None,
            height=dp(35)
        ))

        root.add_widget(Label(
            text="PREMIUM STUDY HUB",
            font_size=sp(13),
            color=MUTED,
            size_hint_y=None,
            height=dp(30)
        ))

        root.add_widget(Label(
            text="━━━━━━━━━━━━━━━━━━━━",
            color=GOLD,
            size_hint_y=None,
            height=dp(25)
        ))

        root.add_widget(Label(
            text="Enter your private study password",
            color=MUTED,
            font_size=sp(14),
            size_hint_y=None,
            height=dp(30)
        ))

        self.password = TextInput(
            hint_text="PASSWORD",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=dp(52),
            font_size=sp(17),
            padding=[dp(18), dp(12)]
        )

        root.add_widget(self.password)

        login = PremiumButton(
            text="🔐  UNLOCK KUZRAT",
            bg_color=GOLD2,
            text_color=BG,
            size_hint_y=None,
            height=dp(55)
        )

        login.bind(on_release=self.check_password)

        root.add_widget(login)

        root.add_widget(Label(
            text="Deep Notes • Practice Papers • Progress",
            color=MUTED,
            font_size=sp(12)
        ))

        self.add_widget(root)

    def check_password(self, instance):

        if self.password.text == "KUZRAT10":
            self.password.text = ""
            self.manager.current = "home"
        else:
            Popup(
                title="Access Denied",
                content=Label(
                    text="Wrong password.\nPlease enter the correct password.",
                    color=WHITE
                ),
                size_hint=(0.8, 0.3)
            ).open()


# ------------------------------------------------------------
# HOME SCREEN
# ------------------------------------------------------------

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main = BoxLayout(
            orientation="vertical",
            spacing=dp(8)
        )

        # HEADER
        header = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(145),
            padding=[dp(18), dp(12)],
            spacing=dp(2)
        )

        title = Label(
            text="👑  KUZRAT",
            color=GOLD,
            font_size=sp(29),
            bold=True,
            size_hint_y=None,
            height=dp(42)
        )

        subtitle = Label(
            text="CLASS 10 • SCIENCE  |  PREMIUM STUDY HUB",
            color=WHITE,
            font_size=sp(13),
            size_hint_y=None,
            height=dp(28)
        )

        tagline = Label(
            text="DEEP NOTES  •  PRACTICE  •  PROGRESS",
            color=MUTED,
            font_size=sp(11),
            size_hint_y=None,
            height=dp(25)
        )

        search = TextInput(
            hint_text="🔍  Search chapters or topics...",
            multiline=False,
            size_hint_y=None,
            height=dp(45),
            font_size=sp(14),
            padding=[dp(14), dp(10)]
        )

        search.bind(text=self.search_chapters)

        header.add_widget(title)
        header.add_widget(subtitle)
        header.add_widget(tagline)
        header.add_widget(search)

        main.add_widget(header)

        # SCROLL AREA
        scroll = ScrollView(
            do_scroll_x=False,
            bar_width=dp(5)
        )

        self.content = GridLayout(
            cols=1,
            spacing=dp(12),
            padding=[dp(15), dp(10)],
            size_hint_y=None
        )

        self.content.bind(
            minimum_height=self.content.setter("height")
        )

        scroll.add_widget(self.content)
        main.add_widget(scroll)

        # BOTTOM BAR
        bottom = BoxLayout(
            size_hint_y=None,
            height=dp(58),
            spacing=dp(7),
            padding=[dp(8), dp(7)]
        )

        home_btn = PremiumButton(
            text="🏠 HOME",
            bg_color=BLUE
        )
        home_btn.bind(on_release=lambda x: None)

        progress_btn = PremiumButton(
            text="🏆 PROGRESS",
            bg_color=PURPLE
        )
        progress_btn.bind(
            on_release=lambda x: self.show_progress()
        )

        lock_btn = PremiumButton(
            text="🔒 LOCK",
            bg_color=RED
        )
        lock_btn.bind(
            on_release=lambda x: self.lock_app()
        )

        bottom.add_widget(home_btn)
        bottom.add_widget(progress_btn)
        bottom.add_widget(lock_btn)

        main.add_widget(bottom)

        self.add_widget(main)

        self.populate()

    def populate(self, filter_text=""):

        self.content.clear_widgets()

        # CHAPTER HEADING
        heading = GoldTitle(
            text="📚  CHAPTERS  •  DEEP NOTES",
            font_size=sp(21),
            size_hint_y=None,
            height=dp(45)
        )

        self.content.add_widget(heading)

        for num, name in CHAPTERS:

            if filter_text:
                if filter_text.lower() not in (
                    num + " " + name
                ).lower():
                    continue

            card = PremiumButton(
                text=f"CHAPTER {num}\n{name}",
                bg_color=CARD,
                text_color=WHITE,
                size_hint_y=None,
                height=dp(75),
                font_size=sp(14)
            )

            card.bind(
                on_release=lambda btn, n=num, title=name:
                self.open_chapter(n, title)
            )

            self.content.add_widget(card)

        # ----------------------------------------------------
        # PRACTICE SETS - UNDER CHAPTERS
        # ----------------------------------------------------

        divider = Label(
            text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            color=GOLD,
            size_hint_y=None,
            height=dp(30)
        )

        self.content.add_widget(divider)

        practice_heading = GoldTitle(
            text="📝  PRACTICE SETS",
            font_size=sp(23),
            size_hint_y=None,
            height=dp(50)
        )

        self.content.add_widget(practice_heading)

        description = Label(
            text="10 PREMIUM FULL PAPERS  •  80 MARKS  •  3 HOURS 15 MINUTES",
            color=MUTED,
            font_size=sp(11),
            size_hint_y=None,
            height=dp(32)
        )

        self.content.add_widget(description)

        # Two cards per row
        practice_grid = GridLayout(
            cols=2,
            spacing=dp(10),
            size_hint_y=None
        )

        practice_grid.bind(
            minimum_height=practice_grid.setter("height")
        )

        for i in range(1, 11):

            paper_btn = PremiumButton(
                text=(
                    f"📝  PRACTICE SET {i}\n"
                    f"80 MARKS  •  3H 15M"
                ),
                bg_color=(
                    BLUE if i % 2 else PURPLE
                ),
                text_color=WHITE,
                size_hint_y=None,
                height=dp(90),
                font_size=sp(13)
            )

            paper_btn.bind(
                on_release=lambda btn, no=i:
                self.open_paper(no)
            )

            practice_grid.add_widget(paper_btn)

        self.content.add_widget(practice_grid)

        # IMPORTANT TOPICS
        self.content.add_widget(
            Label(
                text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                color=GOLD,
                size_hint_y=None,
                height=dp(30)
            )
        )

        important = PremiumButton(
            text="⭐  IMPORTANT TOPICS",
            bg_color=GOLD2,
            text_color=BG,
            size_hint_y=None,
            height=dp(55)
        )

        important.bind(
            on_release=lambda x: self.show_important()
        )

        self.content.add_widget(important)

    def search_chapters(self, instance, text):
        self.populate(text)

    def open_chapter(self, num, title):

        screen = self.manager.get_screen("content")

        screen.set_content(
            f"CHAPTER {num}\n{title}",
            NOTES.get(num, "Notes coming soon.")
        )

        self.manager.current = "content"

    def open_paper(self, number):

        screen = self.manager.get_screen("paper")

        screen.load_paper(number)

        self.manager.current = "paper"

    def show_progress(self):

        Popup(
            title="🏆 KUZRAT PROGRESS",
            content=Label(
                text=(
                    "YOUR STUDY DASHBOARD\n\n"
                    "📚 Chapters: 14\n"
                    "📝 Practice Sets: 10\n"
                    "🎯 Full Marks: 80 per paper\n\n"
                    "Keep studying consistently!"
                ),
                color=WHITE,
                halign="center"
            ),
            size_hint=(0.85, 0.55)
        ).open()

    def show_important(self):

        text = """
⭐ IMPORTANT TOPICS

CHEMISTRY
• Balancing equations
• Types of reactions
• pH
• Salts
• Reactivity series
• Carbon compounds

BIOLOGY
• Photosynthesis
• Digestion
• Circulation
• Excretion
• Reproduction
• Mendel genetics
• Ecosystem

PHYSICS
• Mirror formula
• Lens formula
• Eye defects
• Ohm's law
• Electricity numericals
• Motor
• Generator
• Sources of energy

🔥 FOCUS:
Definitions + diagrams + equations +
numericals + NCERT-based concepts.
"""

        screen = self.manager.get_screen("content")
        screen.set_content(
            "IMPORTANT TOPICS",
            text
        )
        self.manager.current = "content"

    def lock_app(self):
        self.manager.current = "login"


# ------------------------------------------------------------
# CONTENT / NOTES SCREEN
# ------------------------------------------------------------

class ContentScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            spacing=dp(8)
        )

        self.title = Label(
            text="KUZRAT NOTES",
            color=GOLD,
            font_size=sp(21),
            bold=True,
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.title)

        scroll = ScrollView(
            do_scroll_x=False
        )

        self.text_label = Label(
            text="",
            color=WHITE,
            font_size=sp(14),
            halign="left",
            valign="top",
            padding=[dp(18), dp(15)],
            size_hint_y=None
        )

        self.text_label.bind(
            texture_size=self.text_label.setter("size")
        )

        scroll.add_widget(self.text_label)

        root.add_widget(scroll)

        back = PremiumButton(
            text="←  BACK TO HOME",
            bg_color=BLUE,
            size_hint_y=None,
            height=dp(52)
        )

        back.bind(
            on_release=lambda x:
            setattr(self.manager, "current", "home")
        )

        root.add_widget(back)

        self.add_widget(root)

    def set_content(self, title, text):

        self.title.text = "📖  " + title
        self.text_label.text = text


# ------------------------------------------------------------
# PAPER SCREEN
# ------------------------------------------------------------

class PaperScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            spacing=dp(6)
        )

        self.header = Label(
            text="PRACTICE PAPER",
            color=GOLD,
            font_size=sp(22),
            bold=True,
            size_hint_y=None,
            height=dp(58)
        )

        root.add_widget(self.header)

        scroll = ScrollView(
            do_scroll_x=False
        )

        self.paper_text = Label(
            text="",
            color=WHITE,
            font_size=sp(13),
            halign="left",
            valign="top",
            padding=[dp(16), dp(12)],
            size_hint_y=None
        )

        self.paper_text.bind(
            texture_size=self.paper_text.setter("size")
        )

        scroll.add_widget(self.paper_text)

        root.add_widget(scroll)

        bottom = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(7),
            padding=[dp(7), dp(5)]
        )

        back = PremiumButton(
            text="← HOME",
            bg_color=BLUE
        )

        back.bind(
            on_release=lambda x:
            setattr(self.manager, "current", "home")
        )

        answer = PremiumButton(
            text="✅ ANSWER KEY",
            bg_color=GREEN
        )

        answer.bind(
            on_release=lambda x:
            self.show_answers()
        )

        bottom.add_widget(back)
        bottom.add_widget(answer)

        root.add_widget(bottom)

        self.add_widget(root)

        self.current_number = 1

    def load_paper(self, number):

        self.current_number = number

        paper = PAPERS[number]

        lines = []

        lines.append(
            f"""
╔══════════════════════════════════╗
        KUZRAT PREMIUM
        PRACTICE SET {number}
╚══════════════════════════════════╝

CLASS: 10 SCIENCE
MAXIMUM MARKS: 80
TIME: 3 HOURS 15 MINUTES

Physics + Chemistry + Biology
========================================

SECTION A
MCQ — 18 × 1 = 18 MARKS
"""
        )

        for i, q in enumerate(paper["mcqs"], 1):

            question, options, ans = q

            lines.append(
                f"\nQ{i}. {question}\n"
                f"   A) {options[0]}\n"
                f"   B) {options[1]}\n"
                f"   C) {options[2]}\n"
                f"   D) {options[3]}\n"
            )

        lines.append(
            """

SECTION A — PART 2
FILL IN THE BLANKS
6 × 1 = 6 MARKS

Q19. The pH of a neutral solution is ______.
Q20. The functional unit of kidney is ______.
Q21. The SI unit of current is ______.
Q22. The genetic material is ______.
Q23. The major component of biogas is ______.
Q24. Myopia is corrected by a ______ lens.


SECTION A — PART 3
ONE SENTENCE ANSWERS
12 × 1 = 12 MARKS

Q25. What is oxidation?
Q26. What is a neutralisation reaction?
Q27. What is an alloy?
Q28. Define catenation.
Q29. What is photosynthesis?
Q30. What is a reflex action?
Q31. What is fertilisation?
Q32. What is a gene?
Q33. What is biomagnification?
Q34. State one law of reflection.
Q35. State Ohm's law.
Q36. What is electromagnetic induction?


SECTION B
SHORT ANSWER QUESTIONS
10 × 2 = 20 MARKS
"""
        )

        for i, q in enumerate(paper["short"], 37):
            lines.append(f"\nQ{i}. {q}\n")

        lines.append(
            """

SECTION C
LONG ANSWER QUESTIONS
4 × 3 = 12 MARKS
"""
        )

        for i, q in enumerate(paper["long"][:4], 49):
            lines.append(f"\nQ{i}. {q}\n")

        lines.append(
            """

SECTION D
VERY LONG ANSWER QUESTIONS
3 × 4 = 12 MARKS
"""
        )

        for i, q in enumerate(paper["very"][:3], 53):
            lines.append(f"\nQ{i}. {q}\n")

        lines.append(
            """

========================================
                 END
========================================

CHECK:
MCQ 18
FILL 6
ONE SENTENCE 12
SHORT 20
LONG 12
VERY LONG 12

TOTAL = 80 MARKS
"""
        )

        self.header.text = (
            f"📝  PRACTICE SET {number}  •  80 MARKS"
        )

        self.paper_text.text = "".join(lines)

    def show_answers(self):

        answers = """
ANSWER KEY

MCQs:
1. A
2. B
3. C
4. C
5. B
6. A
7. B
8. B
9. C
10. B
11. C
12. B
13. A
14. B
15. B
16. B
17. C
18. A

FILL IN:
19. 7
20. Nephron
21. Ampere
22. DNA
23. Methane
24. Concave

Important formulas:
V = IR
I = Q/t
P = VI
P = I²R
P = V²/R
E = Pt
1 kWh = 3.6 × 10^6 J
1/f = 1/v + 1/u
m = -v/u
P(lens) = 1/f
"""

        Popup(
            title="✅ ANSWER KEY",
            content=ScrollView(
                do_scroll_x=False
            ),
            size_hint=(0.9, 0.8)
        ).open()

        # A clearer second popup for compatibility
        Popup(
            title="KUZRAT • ANSWERS",
            content=Label(
                text=answers,
                color=WHITE,
                halign="left",
                valign="top"
            ),
            size_hint=(0.9, 0.75)
        ).open()


# ------------------------------------------------------------
# APP
# ------------------------------------------------------------

class KuzratApp(App):

    def build(self):

        Window.clearcolor = BG

        sm = ScreenManager(
            transition=FadeTransition(duration=0.15)
        )

        sm.add_widget(
            LoginScreen(name="login")
        )

        sm.add_widget(
            HomeScreen(name="home")
        )

        sm.add_widget(
            ContentScreen(name="content")
        )

        sm.add_widget(
            PaperScreen(name="paper")
        )

        return sm


# ------------------------------------------------------------
# RUN
# ------------------------------------------------------------

if __name__ == "__main__":
    KuzratApp().run()

