const SKILL_SECTIONS = [
    {
        title: "Umiej&#281;tno&#347;ci og&oacute;lne",
        skills: [
            { slug: "alchemia", label: "Alchemia", abbr: "I" },
            { slug: "astrokartografia", label: "Astrokartografia", abbr: "I" },
            { slug: "atletyka", label: "Atletyka", abbr: "K" },
            { slug: "czujnosc", label: "Czujno&#347;&#263;", abbr: "W" },
            { slug: "dyscyplina", label: "Dyscyplina", abbr: "W" },
            { slug: "jezdziectwo", label: "Je&#378;dziectwo", abbr: "Z" },
            { slug: "komputery", label: "Komputery", abbr: "I" },
            { slug: "koordynacja", label: "Koordynacja", abbr: "Z" },
            { slug: "machlojki", label: "Machlojki", abbr: "S" },
            { slug: "mechanika", label: "Mechanika", abbr: "I" },
            { slug: "medycyna", label: "Medycyna", abbr: "I" },
            { slug: "odpornosc", label: "Odporno&#347;&#263;", abbr: "K" },
            { slug: "opanowanie", label: "Opanowanie", abbr: "P" },
            { slug: "percepcja", label: "Percepcja", abbr: "S" },
            { slug: "pilotaz", label: "Pilota&#380;", abbr: "Z" },
            { slug: "pojazdy_zalogowe", label: "Pojazdy za&#322;ogowe", abbr: "I" },
            { slug: "prowadzenie_pojazdow", label: "Prowadzenie pojazd&oacute;w", abbr: "Z" },
            { slug: "sztuka_przetrwania", label: "Sztuka przetrwania", abbr: "S" },
            { slug: "ukrywanie_sie", label: "Ukrywanie si&#281;", abbr: "Z" },
            { slug: "znajomosc_polswiatka", label: "Znajomo&#347;&#263; p&oacute;&#322;&#347;wiatka", abbr: "S" }
        ]
    },
    {
        title: "Umiej&#281;tno&#347;ci magiczne",
        skills: [
            { slug: "moc_boska", label: "Moc boska", abbr: "W" },
            { slug: "moc_pierwotna", label: "Moc pierwotna", abbr: "S" },
            { slug: "moc_tajemna", label: "Moc tajemna", abbr: "I" }
        ]
    },
    {
        title: "Umiej&#281;tno&#347;ci bojowe",
        skills: [
            { slug: "artyleria", label: "Artyleria", abbr: "Z" },
            { slug: "bijatyka", label: "Bijatyka", abbr: "K" },
            { slug: "bron_biala", label: "Bro&#324; bia&#322;a", abbr: "K" },
            { slug: "bron_biala_ciezka", label: "Bro&#324; bia&#322;a (ci&#281;&#380;ka)", abbr: "K" },
            { slug: "bron_biala_lekka", label: "Bro&#324; bia&#322;a (lekka)", abbr: "K" },
            { slug: "bron_dystansowa", label: "Bro&#324; dystansowa", abbr: "Z" },
            { slug: "bron_dystansowa_ciezka", label: "Bro&#324; dystansowa (ci&#281;&#380;ka)", abbr: "Z" },
            { slug: "bron_dystansowa_lekka", label: "Bro&#324; dystansowa (lekka)", abbr: "Z" }
        ]
    },
    {
        title: "Umiej&#281;tno&#347;ci spo&#322;eczne",
        skills: [
            { slug: "negocjacje", label: "Negocjacje", abbr: "P" },
            { slug: "oszustwo", label: "Oszustwo", abbr: "S" },
            { slug: "przymuszanie", label: "Przymuszanie", abbr: "W" },
            { slug: "przywodztwo", label: "Przyw&oacute;dztwo", abbr: "P" },
            { slug: "urok_osobisty", label: "Urok osobisty", abbr: "P" }
        ]
    },
    {
        title: "Umiej&#281;tno&#347;ci akademickie",
        skills: [
            { slug: "wiedza", label: "Wiedza", abbr: "I" },
            { slug: "wiedza_2", label: "Wiedza w&#322;asna 1", abbr: "I", editableLabel: true, editableCharacteristic: true },
            { slug: "wiedza_3", label: "Wiedza w&#322;asna 2", abbr: "I", editableLabel: true, editableCharacteristic: true },
            { slug: "wiedza_4", label: "Wiedza w&#322;asna 3", abbr: "I", editableLabel: true, editableCharacteristic: true }
        ]
    },
    {
        title: "Umiej&#281;tno&#347;ci niestandardowe",
        skills: [
            { slug: "niestandardowa_1", label: "Umiej&#281;tno&#347;&#263; w&#322;asna 1", abbr: "I", editableLabel: true, editableCharacteristic: true },
            { slug: "niestandardowa_2", label: "Umiej&#281;tno&#347;&#263; w&#322;asna 2", abbr: "I", editableLabel: true, editableCharacteristic: true },
            { slug: "niestandardowa_3", label: "Umiej&#281;tno&#347;&#263; w&#322;asna 3", abbr: "I", editableLabel: true, editableCharacteristic: true },
            { slug: "niestandardowa_4", label: "Umiej&#281;tno&#347;&#263; w&#322;asna 4", abbr: "I", editableLabel: true, editableCharacteristic: true }
        ]
    }
];

const ALL_SKILLS = SKILL_SECTIONS.flatMap((section) => section.skills);
const CHARACTERISTIC_OPTIONS = [
    { value: "K", label: "K" },
    { value: "Z", label: "Z" },
    { value: "I", label: "I" },
    { value: "S", label: "S" },
    { value: "W", label: "W" },
    { value: "P", label: "P" }
];
const WEAPON_COLUMNS = [
    { key: "name", label: "Broń" },
    { key: "skill", label: "Umiejętność" },
    { key: "damage", label: "Obrażenia" },
    { key: "crit", label: "Krytyczność" },
    { key: "range", label: "Zasięg" },
    { key: "special", label: "Specjalne" }
];
const TALENT_COLUMNS = [
    { key: "name", label: "Nazwa" },
    { key: "page", label: "Strona" },
    { key: "description", label: "Opis zdolności" }
];

function buildEmptySkillRanks() {
    return Object.fromEntries(ALL_SKILLS.map((skill) => [skill.slug, 0]));
}

function buildEmptyWeaponRows() {
    return Array.from({ length: 4 }, () => ({
        name: "",
        skill: "",
        damage: "",
        crit: "",
        range: "",
        special: ""
    }));
}

function buildEmptyTalentRows() {
    return Array.from({ length: 12 }, () => ({
        name: "",
        page: "",
        description: ""
    }));
}

function buildDefaultSkillLabels() {
    return Object.fromEntries(
        ALL_SKILLS
            .filter((skill) => skill.editableLabel)
            .map((skill) => [skill.slug, ""])
    );
}

function buildDefaultSkillCharacteristics() {
    return Object.fromEntries(
        ALL_SKILLS
            .filter((skill) => skill.editableCharacteristic)
            .map((skill) => [skill.slug, ""])
    );
}

function buildDefaultSkillUniverse() {
    return Object.fromEntries(ALL_SKILLS.map((skill) => [skill.slug, true]));
}

function buildDefaultSkillProfession() {
    return Object.fromEntries(ALL_SKILLS.map((skill) => [skill.slug, false]));
}

const presets = {
    noviceGuard: {
        name: "Stra\u017cnik z Dalan",
        archetype: "Cz\u0142owiek",
        career: "Stra\u017cnik",
        player: "GM",
        brawn: 3,
        agility: 2,
        intellect: 2,
        cunning: 2,
        willpower: 2,
        presence: 2,
        soak: 4,
        woundThreshold: 13,
        strainThreshold: 12,
        meleeDefense: 0,
        rangedDefense: 0,
        current_wounds: 0,
        current_strain: 0,
        skillRanks: {
            ...buildEmptySkillRanks(),
            atletyka: 1,
            bron_biala: 1,
            percepcja: 1
        },
        skillLabels: buildDefaultSkillLabels(),
        skillCharacteristics: buildDefaultSkillCharacteristics(),
        skillUniverse: buildDefaultSkillUniverse(),
        skillProfession: buildDefaultSkillProfession(),
        weaponRows: [
            { name: "Włócznia", skill: "", damage: "", crit: "Kryt 3", range: "Zwarcie", special: "" },
            { name: "Kusza", skill: "", damage: "", crit: "Kryt 4", range: "Średni", special: "" },
            ...buildEmptyWeaponRows().slice(2)
        ],
        talentRows: [
            { name: "Brak", page: "", description: "" },
            ...buildEmptyTalentRows().slice(1)
        ],
        desire: "Taktyka grupowa: dodaje 1 ko\u015b\u0107 premii, gdy dzia\u0142a z innym stra\u017cnikiem.",
        fear: "",
        armor_weapons: "Koszulka kolcza, tarcza, dodatkowy kołczan",
        equipment: "Koszulka kolcza, tarcza, gwizdek, pochodnia",
        sex: "",
        age: "",
        height: "",
        body_build: "",
        hair: "",
        eyes: "",
        distinctive_marks: "",
        notes: "Minion do patroli miejskich. Solidny, ale nie bohaterski."
    },
    streetInformant: {
        name: "Mira Popio\u0142ostopa",
        archetype: "Cz\u0142owiek",
        career: "\u0141otrzyk",
        player: "GM",
        brawn: 2,
        agility: 3,
        intellect: 3,
        cunning: 4,
        willpower: 2,
        presence: 3,
        soak: 3,
        woundThreshold: 12,
        strainThreshold: 11,
        meleeDefense: 0,
        rangedDefense: 1,
        current_wounds: 0,
        current_strain: 0,
        skillRanks: {
            ...buildEmptySkillRanks(),
            oszustwo: 3,
            urok_osobisty: 2,
            znajomosc_polswiatka: 1
        },
        skillLabels: buildDefaultSkillLabels(),
        skillCharacteristics: buildDefaultSkillCharacteristics(),
        skillUniverse: buildDefaultSkillUniverse(),
        skillProfession: buildDefaultSkillProfession(),
        weaponRows: [
            { name: "Pistolet kieszonkowy", skill: "", damage: "", crit: "Kryt 4", range: "Krótki", special: "" },
            { name: "Nóż", skill: "", damage: "", crit: "Kryt 3", range: "Zwarcie", special: "" },
            ...buildEmptyWeaponRows().slice(2)
        ],
        talentRows: [
            { name: "Przekonująca postawa", page: "2", description: "" },
            { name: "Spryt ulicznika", page: "", description: "" },
            ...buildEmptyTalentRows().slice(2)
        ],
        desire: "Kontakty w p\u00f3\u0142\u015bwiatku: raz na sesj\u0119 mo\u017ce zdoby\u0107 u\u017cyteczn\u0105 plotk\u0119 albo trop.",
        fear: "",
        armor_weapons: "Ukryta kabura, lekka kurtka ochronna",
        equipment: "Szyfrowany notatnik, zestaw do przebrania, ukryte kredyty",
        sex: "",
        age: "",
        height: "",
        body_build: "",
        hair: "",
        eyes: "",
        distinctive_marks: "",
        notes: "Najpierw handluje informacjami za przys\u0142ugi, dopiero potem za pieni\u0105dze."
    },
    arcaneRival: {
        name: "Brat Kaldris",
        archetype: "Elf",
        career: "Mag",
        player: "GM",
        brawn: 2,
        agility: 2,
        intellect: 4,
        cunning: 3,
        willpower: 4,
        presence: 3,
        soak: 3,
        woundThreshold: 11,
        strainThreshold: 14,
        meleeDefense: 0,
        rangedDefense: 1,
        current_wounds: 0,
        current_strain: 0,
        skillRanks: {
            ...buildEmptySkillRanks(),
            moc_tajemna: 3,
            dyscyplina: 2,
            wiedza: 2
        },
        skillLabels: {
            ...buildDefaultSkillLabels(),
            wiedza_2: "Wiedza (legendy)",
            wiedza_3: "Wiedza (magia)",
            wiedza_4: "Wiedza (historia)",
            niestandardowa_1: "Rytualy",
            niestandardowa_2: "Runy"
        },
        skillCharacteristics: {
            ...buildDefaultSkillCharacteristics(),
            wiedza_2: "I",
            wiedza_3: "I",
            wiedza_4: "I",
            niestandardowa_1: "W",
            niestandardowa_2: "I"
        },
        skillUniverse: buildDefaultSkillUniverse(),
        skillProfession: buildDefaultSkillProfession(),
        weaponRows: [
            { name: "Runiczna laska", skill: "", damage: "", crit: "Kryt 3", range: "Zwarcie", special: "" },
            { name: "Zaklęcie ataku", skill: "", damage: "", crit: "Kryt 3", range: "Średni", special: "" },
            ...buildEmptyWeaponRows().slice(2)
        ],
        talentRows: [
            { name: "Przeciwnik", page: "1", description: "" },
            { name: "Lepsza koncentracja", page: "", description: "" },
            ...buildEmptyTalentRows().slice(2)
        ],
        desire: "Skupienie zakl\u0119\u0107: mo\u017ce otrzyma\u0107 2 zm\u0119czenia, aby raz na tur\u0119 obni\u017cy\u0107 trudno\u015b\u0107 zakl\u0119cia.",
        fear: "",
        armor_weapons: "Magiczne bariery, runiczna laska, amulety ochronne",
        equipment: "Ksi\u0119ga zakl\u0119\u0107, szaty, amulety, kreda alchemiczna",
        sex: "",
        age: "",
        height: "",
        body_build: "",
        hair: "",
        eyes: "",
        distinctive_marks: "",
        notes: "Dobrze dzia\u0142a jako powracaj\u0105cy magiczny antagonista albo niepewny sojusznik."
    }
};

const customBlankState = {
    name: "",
    archetype: "",
    career: "",
    player: "",
    brawn: 2,
    agility: 2,
    intellect: 2,
    cunning: 2,
    willpower: 2,
    presence: 2,
    soak: 2,
    woundThreshold: 12,
    strainThreshold: 12,
    meleeDefense: 0,
    rangedDefense: 0,
    current_wounds: 0,
    current_strain: 0,
    skillRanks: buildEmptySkillRanks(),
    skillLabels: buildDefaultSkillLabels(),
    skillCharacteristics: buildDefaultSkillCharacteristics(),
    skillUniverse: buildDefaultSkillUniverse(),
    skillProfession: buildDefaultSkillProfession(),
    weaponRows: buildEmptyWeaponRows(),
    talentRows: buildEmptyTalentRows(),
    advantage: "",
    flaw: "",
    desire: "",
    fear: "",
    armor_weapons: "",
    equipment: "",
    sex: "",
    age: "",
    height: "",
    body_build: "",
    hair: "",
    eyes: "",
    distinctive_marks: "",
    notes: ""
};
const defaultState = structuredClone(customBlankState);

const form = document.getElementById("sheet-form");
const jsonOutput = document.getElementById("json-output");
const backendStatus = document.getElementById("backend-status");
const backendStatusMessage = backendStatus.querySelector(".toast-message");
const generatePdfButton = document.getElementById("generate-pdf");
const skillsEditor = document.getElementById("skills-editor");
const weaponsEditor = document.getElementById("weapons-editor");
const talentsEditor = document.getElementById("talents-editor");
let toastTimerId = null;

function skillFieldName(slug) {
    return `skill_rank__${slug}`;
}

function skillLabelFieldName(slug) {
    return `skill_label__${slug}`;
}

function skillCharacteristicFieldName(slug) {
    return `skill_characteristic__${slug}`;
}

function skillUniverseFieldName(slug) {
    return `skill_universe__${slug}`;
}

function skillProfessionFieldName(slug) {
    return `skill_profession__${slug}`;
}

function weaponFieldName(index, key) {
    return `weapon__${index}__${key}`;
}

function talentFieldName(index, key) {
    return `talent__${index}__${key}`;
}

function decodeHtml(value) {
    const textarea = document.createElement("textarea");
    textarea.innerHTML = value;
    return textarea.value;
}

function renderSkillsEditor() {
    skillsEditor.innerHTML = SKILL_SECTIONS.map((section) => `
        <section class="skill-card">
            <header class="skill-card-header">
                <h3>${section.title}</h3>
                <span>Poziom 0-5</span>
            </header>
            <div class="skill-list">
                ${section.skills.map((skill) => `
                    <div class="skill-row ${skill.editableLabel ? "is-custom" : ""}">
                        <div class="skill-meta">
                            ${skill.editableLabel
                                ? `<label class="skill-label-field">
                                        <span>Nazwa umiej&#281;tno&#347;ci</span>
                                        <input type="text" class="skill-label-input" name="${skillLabelFieldName(skill.slug)}" value="">
                                   </label>`
                                : `<span class="skill-name">${skill.label} <em>(${skill.abbr})</em></span>`}
                            ${skill.editableCharacteristic
                                ? `<label class="skill-mini">
                                        <span>Cecha</span>
                                        <select name="${skillCharacteristicFieldName(skill.slug)}">
                                            <option value="" selected></option>
                                            ${CHARACTERISTIC_OPTIONS.map((option) => `<option value="${option.value}">${option.label}</option>`).join("")}
                                        </select>
                                   </label>`
                                : ""}
                            <div class="skill-flags">
                                <label class="skill-check">
                                    <input type="checkbox" name="${skillUniverseFieldName(skill.slug)}" checked>
                                    <span>Uniwersum?</span>
                                </label>
                                <label class="skill-check">
                                    <input type="checkbox" name="${skillProfessionFieldName(skill.slug)}">
                                    <span>Profesja?</span>
                                </label>
                            </div>
                        </div>
                        <label class="skill-mini">
                            <span>Poziom</span>
                            <select name="${skillFieldName(skill.slug)}" data-skill-rank="${skill.slug}">
                                <option value="0">0</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                            </select>
                        </label>
                    </div>
                `).join("")}
            </div>
        </section>
    `).join("");
}

function renderWeaponsEditor() {
    const firstRowPlaceholders = {
        name: "np. Pistolet kieszonkowy",
        skill: "np. Lekka dystansowa",
        damage: "np. 6",
        crit: "np. Kryt 4",
        range: "np. Krótki",
        special: "np. Ukryta, Ogłuszająca"
    };

    weaponsEditor.innerHTML = `
        <div class="weapons-table">
            <div class="weapons-header">
                ${WEAPON_COLUMNS.map((column) => `<span>${column.label}</span>`).join("")}
            </div>
            <div class="weapons-body">
                ${Array.from({ length: 4 }, (_, rowIndex) => `
                    <div class="weapons-row">
                        ${WEAPON_COLUMNS.map((column) => `
                            <input
                                type="text"
                                name="${weaponFieldName(rowIndex, column.key)}"
                                placeholder="${rowIndex === 0 ? firstRowPlaceholders[column.key] : ""}"
                            >
                        `).join("")}
                    </div>
                `).join("")}
            </div>
        </div>
    `;
}

function renderTalentsEditor() {
    const firstRowPlaceholders = {
        name: "Robienie w chuja",
        page: "np. 2",
        description: "Krótki opis działania talentu albo zdolności"
    };

    talentsEditor.innerHTML = `
        <div class="talents-table">
            <div class="talents-header">
                ${TALENT_COLUMNS.map((column) => `<span>${column.label}</span>`).join("")}
            </div>
            <div class="talents-body">
                ${Array.from({ length: 12 }, (_, rowIndex) => `
                    <div class="talents-row">
                        ${TALENT_COLUMNS.map((column) => `
                            <input
                                type="text"
                                name="${talentFieldName(rowIndex, column.key)}"
                                placeholder="${rowIndex === 0 ? firstRowPlaceholders[column.key] : ""}"
                            >
                        `).join("")}
                    </div>
                `).join("")}
            </div>
        </div>
    `;
}

function normalizeNumber(value, fallback = 0) {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : fallback;
}

function applySkillRanks(skillRanks = {}) {
    ALL_SKILLS.forEach((skill) => {
        const field = form.elements.namedItem(skillFieldName(skill.slug));
        if (field) {
            field.value = normalizeNumber(skillRanks[skill.slug], 0);
        }
    });
}

function applySkillLabels(skillLabels = {}) {
    ALL_SKILLS.filter((skill) => skill.editableLabel).forEach((skill) => {
        const field = form.elements.namedItem(skillLabelFieldName(skill.slug));
        if (field) {
            field.value = skillLabels[skill.slug] || "";
        }
    });
}

function applySkillCharacteristics(skillCharacteristics = {}) {
    ALL_SKILLS.filter((skill) => skill.editableCharacteristic).forEach((skill) => {
        const field = form.elements.namedItem(skillCharacteristicFieldName(skill.slug));
        if (field) {
            field.value = skillCharacteristics[skill.slug] || "";
        }
    });
}

function applySkillUniverse(skillUniverse = {}) {
    ALL_SKILLS.forEach((skill) => {
        const field = form.elements.namedItem(skillUniverseFieldName(skill.slug));
        if (field) {
            field.checked = skillUniverse[skill.slug] !== undefined ? Boolean(skillUniverse[skill.slug]) : true;
        }
    });
}

function applySkillProfession(skillProfession = {}) {
    ALL_SKILLS.forEach((skill) => {
        const field = form.elements.namedItem(skillProfessionFieldName(skill.slug));
        if (field) {
            field.checked = skillProfession[skill.slug] !== undefined ? Boolean(skillProfession[skill.slug]) : false;
        }
    });
}

function applyWeaponRows(weaponRows = []) {
    const rows = Array.isArray(weaponRows) ? weaponRows : [];
    for (let rowIndex = 0; rowIndex < 4; rowIndex += 1) {
        const row = rows[rowIndex] || {};
        WEAPON_COLUMNS.forEach((column) => {
            const field = form.elements.namedItem(weaponFieldName(rowIndex, column.key));
            if (field) {
                field.value = row[column.key] || "";
            }
        });
    }
}

function applyTalentRows(talentRows = []) {
    const rows = Array.isArray(talentRows) ? talentRows : [];
    for (let rowIndex = 0; rowIndex < 12; rowIndex += 1) {
        const row = rows[rowIndex] || {};
        TALENT_COLUMNS.forEach((column) => {
            const field = form.elements.namedItem(talentFieldName(rowIndex, column.key));
            if (field) {
                field.value = row[column.key] || "";
            }
        });
    }
}

function applyData(data) {
    Object.entries(data).forEach(([key, value]) => {
        if (["skillRanks", "skill_ranks", "skillLabels", "skill_labels", "skillCharacteristics", "skill_characteristics", "skillUniverse", "skill_universe", "skillProfession", "skill_profession", "weaponRows", "weapon_rows", "talentRows", "talent_rows"].includes(key)) {
            return;
        }
        const field = form.elements.namedItem(key);
        if (field) {
            field.value = value;
        }
    });

    applySkillRanks(data.skillRanks || data.skill_ranks || {});
    applySkillLabels(data.skillLabels || data.skill_labels || {});
    applySkillCharacteristics(data.skillCharacteristics || data.skill_characteristics || {});
    applySkillUniverse(data.skillUniverse || data.skill_universe || {});
    applySkillProfession(data.skillProfession || data.skill_profession || {});
    applyWeaponRows(data.weaponRows || data.weapon_rows || []);
    applyTalentRows(data.talentRows || data.talent_rows || []);
    updateDerivedFields();
    render();
}

function updateDerivedFields() {
    const brawn = normalizeNumber(form.elements.brawn.value, 1);
    const willpower = normalizeNumber(form.elements.willpower.value, 1);

    if (!form.elements.soak.dataset.manual) {
        form.elements.soak.value = brawn;
    }

    if (!form.elements.woundThreshold.dataset.manual) {
        form.elements.woundThreshold.value = brawn + 10;
    }

    if (!form.elements.strainThreshold.dataset.manual) {
        form.elements.strainThreshold.value = willpower + 10;
    }
}

function getSkillRanks() {
    const ranks = {};
    ALL_SKILLS.forEach((skill) => {
        const field = form.elements.namedItem(skillFieldName(skill.slug));
        ranks[skill.slug] = normalizeNumber(field?.value, 0);
    });
    return ranks;
}

function getSkillLabels() {
    const labels = {};
    ALL_SKILLS.filter((skill) => skill.editableLabel).forEach((skill) => {
        const field = form.elements.namedItem(skillLabelFieldName(skill.slug));
        labels[skill.slug] = field?.value.trim() || "";
    });
    return labels;
}

function getSkillCharacteristics() {
    const characteristics = {};
    ALL_SKILLS.filter((skill) => skill.editableCharacteristic).forEach((skill) => {
        const field = form.elements.namedItem(skillCharacteristicFieldName(skill.slug));
        characteristics[skill.slug] = field?.value || skill.abbr;
    });
    return characteristics;
}

function getSkillUniverse() {
    const values = {};
    ALL_SKILLS.forEach((skill) => {
        const field = form.elements.namedItem(skillUniverseFieldName(skill.slug));
        values[skill.slug] = Boolean(field?.checked);
    });
    return values;
}

function getSkillProfession() {
    const values = {};
    ALL_SKILLS.forEach((skill) => {
        const field = form.elements.namedItem(skillProfessionFieldName(skill.slug));
        values[skill.slug] = Boolean(field?.checked);
    });
    return values;
}

function getWeaponRows() {
    return Array.from({ length: 4 }, (_, rowIndex) => {
        const row = {};
        WEAPON_COLUMNS.forEach((column) => {
            const field = form.elements.namedItem(weaponFieldName(rowIndex, column.key));
            row[column.key] = field?.value.trim() || "";
        });
        return row;
    });
}

function getTalentRows() {
    return Array.from({ length: 12 }, (_, rowIndex) => {
        const row = {};
        TALENT_COLUMNS.forEach((column) => {
            const field = form.elements.namedItem(talentFieldName(rowIndex, column.key));
            row[column.key] = field?.value.trim() || "";
        });
        return row;
    });
}

function getFormData() {
    const formData = new FormData(form);
    const data = {};

    for (const [key, value] of formData.entries()) {
        if (key.startsWith("skill_rank__") || key.startsWith("skill_universe__") || key.startsWith("skill_profession__")) {
            continue;
        }

        const field = form.elements[key];
        if (field.type === "number") {
            data[key] = normalizeNumber(value);
        } else {
            data[key] = value.trim();
        }
    }

    data.skillRanks = getSkillRanks();
    data.skillLabels = getSkillLabels();
    data.skillCharacteristics = getSkillCharacteristics();
    data.skillUniverse = getSkillUniverse();
    data.skillProfession = getSkillProfession();
    data.weaponRows = getWeaponRows();
    data.talentRows = getTalentRows();
    return data;
}

function render() {
    jsonOutput.value = JSON.stringify(getFormData(), null, 2);
}

function setStatus(message, type = "") {
    backendStatusMessage.textContent = message;
    backendStatus.className = "toast is-visible";
    if (type) {
        backendStatus.classList.add(type);
    }

    if (toastTimerId) {
        window.clearTimeout(toastTimerId);
    }

    if (type !== "error") {
        toastTimerId = window.setTimeout(() => {
            backendStatus.classList.remove("is-visible");
        }, 3400);
    }
}

function setGenerateEnabled(enabled) {
    generatePdfButton.disabled = !enabled;
}

async function inspectSelectedTemplate() {
    try {
        setStatus("Sprawdzanie pliku PDF z folderu template...", "success");
        const response = await fetch("/api/inspect-template", {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });
        const payload = await response.json();
        if (!response.ok) {
            throw new Error(payload.error || "Nie udalo sie sprawdzic szablonu.");
        }

        if (!payload.editable) {
            setStatus(`Szablon ${payload.templateName} nie jest edytowalnym PDF-em.`, "error");
            setGenerateEnabled(false);
            return;
        }

        setStatus(
            `Szablon ${payload.templateName} jest poprawnym formularzem PDF. Zapisano opis pol do ${payload.outputPath}.`,
            "success"
        );
        setGenerateEnabled(true);
    } catch (error) {
        console.error(error);
        setStatus(`Nie udalo sie sprawdzic szablonu: ${error.message}`, "error");
        setGenerateEnabled(false);
    }
}

function markManual(event) {
    const autoDerivedFields = ["soak", "woundThreshold", "strainThreshold"];
    if (autoDerivedFields.includes(event.target.name)) {
        event.target.dataset.manual = "true";
    }
}

function resetDerivedAutoMode() {
    ["soak", "woundThreshold", "strainThreshold"].forEach((name) => {
        delete form.elements[name].dataset.manual;
    });
}

function handleFormMutation(event) {
    markManual(event);
    updateDerivedFields();
    render();
}

function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    link.click();
    URL.revokeObjectURL(url);
}

form.addEventListener("input", handleFormMutation);
form.addEventListener("change", handleFormMutation);

document.getElementById("new-custom").addEventListener("click", () => {
    resetDerivedAutoMode();
    applyData(customBlankState);
});

document.getElementById("export-json").addEventListener("click", () => {
    const blob = new Blob([jsonOutput.value], { type: "application/json" });
    const filename = `${(form.elements.name.value || "karta-postaci").replace(/\s+/g, "-").toLowerCase()}.json`;
    downloadBlob(blob, filename);
});

document.getElementById("copy-json").addEventListener("click", async () => {
    try {
        await navigator.clipboard.writeText(jsonOutput.value);
        setStatus("Skopiowano JSON do schowka.", "success");
    } catch (error) {
        console.error("Clipboard copy failed", error);
        setStatus("Nie udalo sie skopiowac do schowka. Nadal mozesz skopiowac dane recznie z pola JSON.", "error");
    }
});

document.getElementById("save-json").addEventListener("click", async () => {
    try {
        const response = await fetch("/api/save-json", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ character: getFormData() })
        });
        const payload = await response.json();
        if (!response.ok) {
            throw new Error(payload.error || "JSON save failed.");
        }
        setStatus(`Zapisano JSON do characters/${payload.filename}.`, "success");
    } catch (error) {
        console.error(error);
        setStatus(`Nie udalo sie zapisac JSON: ${error.message}`, "error");
    }
});

document.getElementById("generate-pdf").addEventListener("click", async () => {
    try {
        setStatus("Generowanie PDF...", "success");
        const response = await fetch("/api/generate-pdf", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ character: getFormData() })
        });

        if (!response.ok) {
            let message = "PDF generation failed.";
            try {
                const payload = await response.json();
                message = payload.error || message;
            } catch (error) {
                console.error("Could not parse error response", error);
            }
            throw new Error(message);
        }

        const blob = await response.blob();
        const filename = `${(form.elements.name.value || "karta-postaci").replace(/\s+/g, "-").toLowerCase()}.pdf`;
        downloadBlob(blob, filename);
        setStatus("PDF zostal wygenerowany i pobrany.", "success");
    } catch (error) {
        console.error(error);
        setStatus(`Nie udalo sie wygenerowac PDF: ${error.message}`, "error");
    }
});

document.getElementById("reset-sheet").addEventListener("click", () => {
    resetDerivedAutoMode();
    applyData(defaultState);
});

async function checkBackend() {
    try {
        const response = await fetch("/api/health");
        const payload = await response.json();
        if (!response.ok || !payload.ok) {
            throw new Error(payload.error || "Backend unavailable.");
        }

        if (payload.templateExists) {
            setStatus("Lokalny backend Pythona jest gotowy. Wykorzystany zostanie jedyny plik PDF z folderu template.", "success");
        } else {
            setStatus(`Backend dziala, ale nie znaleziono pliku PDF pod sciezka ${payload.templatePath}.`, "error");
        }
    } catch (error) {
        setStatus("Backend jest nieosiagalny. Uruchom Flask poleceniem: python app.py", "error");
    }
}

renderSkillsEditor();
renderWeaponsEditor();
renderTalentsEditor();
applyData(defaultState);
checkBackend();
inspectSelectedTemplate();
