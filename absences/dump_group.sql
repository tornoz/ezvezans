PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
INSERT INTO "auth_group" VALUES(1,'enseignant');
INSERT INTO "auth_group" VALUES(2,'etudiant');
INSERT INTO "auth_group" VALUES(3,'secretaire');
COMMIT;
