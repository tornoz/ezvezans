PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NOT NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL
);
INSERT INTO "auth_user" VALUES(2,'pbkdf2_sha256$12000$FczR3jWbZnJs$iRZk4JmHvo32hK6gAN7ngQWGDGrlFIbQo960wzzCwcs=','2014-02-14 15:02:34.126390',1,'admin','','','admin@admin.admin',1,1,'2014-02-14 08:23:18.319424');
INSERT INTO "auth_user" VALUES(3,'pbkdf2_sha256$12000$OPOA92PosYql$CagpM8cNQOA9Fg1ykcLbNYW458OTxUqNLVyQ2jNB1yk=','2014-02-14 15:03:20',0,'hpotter','Harry','Potter','h.potter@hogwarts.co.uk',0,1,'2014-02-14 15:03:20');
INSERT INTO "auth_user" VALUES(4,'pbkdf2_sha256$12000$kou7fEJ87PVp$IKBx1a0mQqGX5hNol8POfiLyIo9nv6Pk9+6F/bwMTEo=','2014-02-14 15:04:31',0,'rweasley','Ronald','Weasley','r.weasley@hogwarts.co.uk',0,1,'2014-02-14 15:04:31');
INSERT INTO "auth_user" VALUES(5,'pbkdf2_sha256$12000$lgZ1llfR9L95$qj0wmPu2KVh+I1+5mt2SnATWoNpXP8kmhY6H3upHZ+8=','2014-02-14 15:05:12',0,'hgranger','Hermione','Granger','h.granger@hogwarts.co.uk',0,1,'2014-02-14 15:05:12');
INSERT INTO "auth_user" VALUES(6,'pbkdf2_sha256$12000$4FUlrDnA3eDu$PeTWhfIrWhTY06sRUxlVtvhcNVEQEWxz+lVstOMiVHA=','2014-02-14 15:05:52',0,'dmalefoy','Drago','Malefoy','d.malefoy@hogwarts.co.uk',0,1,'2014-02-14 15:05:52');
INSERT INTO "auth_user" VALUES(7,'pbkdf2_sha256$12000$24swI7gFcmm9$m1U510vabRhA7a0ncgH2+2d93i/uK/F9Bs474RJ3L1I=','2014-02-14 15:06:48',0,'nlondubat','Neville','Londubat','n.londubat@hogwarts.co.uk',0,1,'2014-02-14 15:06:48');
INSERT INTO "auth_user" VALUES(8,'pbkdf2_sha256$12000$Rfk1OU8LVNoD$KWyl/9UAOlSTlhsoqjKKN8W3ttEbkQWNL1dxuXSSBkQ=','2014-02-14 15:07:39',0,'eelric','Edward','Elric','e.elric@fma.jp',0,1,'2014-02-14 15:07:39');
INSERT INTO "auth_user" VALUES(9,'pbkdf2_sha256$12000$dKYtYhUbvsPE$zw5zPcRNav086xAKA83uWNnC3uXyudkHv3COM1D1d6U=','2014-02-14 15:08:38',0,'bsummers','Buffy','Summers','b.summers@sunnydale.us',0,1,'2014-02-14 15:08:38');
INSERT INTO "auth_user" VALUES(10,'pbkdf2_sha256$12000$L9pP8iG0x4MH$ZkZxLGtAB5vJlgW2JYiVD88kucLUKzYjaYl6d6dgfHs=','2014-02-14 15:09:42',0,'aharris','Alexander','Harris','a.harris@sunnydale.us',0,1,'2014-02-14 15:09:42');
INSERT INTO "auth_user" VALUES(11,'pbkdf2_sha256$12000$U6qjSd3H3LH7$6gc32VEPvnYxxBS1kcfwF9JSHnEpwt5etRVwYxCwm10=','2014-02-14 15:11:16',0,'cchase','Cordelia','Chase','c.chase@sunnydale.us',0,1,'2014-02-14 15:11:16');
INSERT INTO "auth_user" VALUES(12,'pbkdf2_sha256$12000$ZadeQPD7QjiA$GC4PXCNFlzJu+pZqfd17sCcaP0LEOVbXM4opXcvRhsk=','2014-02-14 15:12:29',0,'wrosenberg','Willow','Rosenberg','w.rosenberg@sunnydale.us',0,1,'2014-02-14 15:12:29');
INSERT INTO "auth_user" VALUES(13,'pbkdf2_sha256$12000$XLQOy7THf1uV$gsujHqZgI6VEtk2yGKkvzO4oIvdA9jOZ9f1SOMbPeTQ=','2014-02-14 15:13:13',0,'srogue','Severus','Rogue','s.rogue@hogwarts.co.uk',0,1,'2014-02-14 15:13:13');
INSERT INTO "auth_user" VALUES(14,'pbkdf2_sha256$12000$BhHRHEjISeBO$45oosK4acHCb/jAf7odGIH1n1f9rJLzhTDp4zq8HLLg=','2014-02-14 15:14:00',0,'adumbledore','Albus','Dumbledore','a.dumbledore@hogwarts.co.uk',0,1,'2014-02-14 15:14:00');
INSERT INTO "auth_user" VALUES(15,'pbkdf2_sha256$12000$OWY6ueIEJjfn$hzfkMXk/185AdgjoG1NT0lzAnVuFhrNBn8wxui7hakQ=','2014-02-14 15:15:34',0,'mmcgonagal','Minerva','McGonagal','m.mcgonagal@hogwarts.co.uk',0,1,'2014-02-14 15:15:34');
INSERT INTO "auth_user" VALUES(16,'pbkdf2_sha256$12000$9nGSMIk7wMjP$VZy6kJ/lx5X9jTbdGrlXHYRrpqu5uWB2Joi72CtV0zk=','2014-02-14 15:16:35',0,'xquirel','Xavier','Quirel','x.quirel@hogwarts.co.uk',0,1,'2014-02-14 15:16:35');
INSERT INTO "auth_user" VALUES(17,'pbkdf2_sha256$12000$otVvOqKnc6fY$skj7YuTzqxwZnR6YdcmKxZI9HayyVYzJCdZRGsYrXJE=','2014-02-14 15:17:36',0,'dmorgandofer','Daria','Morgandofer','d.morgandofer@lonedale.us',0,1,'2014-02-14 15:17:36');
INSERT INTO "auth_user" VALUES(18,'pbkdf2_sha256$12000$oiYa4ACdJNNT$d5hzdTTE6luyLKk7gCogeSJVd3SYqwIuqsr5FSLaPlU=','2014-02-14 15:19:24',0,'rgiles','Rupert','Giles','r.giles@sunnydale.us',0,1,'2014-02-14 15:19:24');
INSERT INTO "auth_user" VALUES(19,'pbkdf2_sha256$12000$mceRaDfDVZ6F$dzXSku85PT/2AEPGC5Fk81cPZqTlDTiV4+L5B0xxJZU=','2014-02-14 15:20:19',0,'jduplantier','Joseph','Duplantier','j.duplantier@gojira.fr',0,1,'2014-02-14 15:20:19');
INSERT INTO "auth_user" VALUES(20,'pbkdf2_sha256$12000$Bx6Z6o0piXdq$HUddhwvIkPgV0hAquq4asuwhKPEDyiJccPFH9JNNboc=','2014-02-14 15:21:35',0,'mduplantier','Mario','Duplantier','m.duplantier@gojira.fr',0,1,'2014-02-14 15:21:35');
INSERT INTO "auth_user" VALUES(21,'pbkdf2_sha256$12000$lAmh9CoAP2LG$PxqBR5SsvgEx4KG+SkVE0DynTgpXjzb3hFKqgL0f9zk=','2014-02-14 15:22:27',0,'jmlabadie','Jean-Michel','Labadie','jm.labadie@gojira.fr',0,1,'2014-02-14 15:22:27');
INSERT INTO "auth_user" VALUES(22,'pbkdf2_sha256$12000$zFmKa2YMYN4k$NC57te+77kYmA052uMcQYoOPiRhsDKUOBo9BIdMFHvM=','2014-02-14 15:23:03',0,'candreu','Chrisitan','Andreu','c.andreu@gojira.fr',0,1,'2014-02-14 15:23:03');
INSERT INTO "auth_user" VALUES(23,'pbkdf2_sha256$12000$A8ZLIOx1k4XI$Mi8EM6RwgJJ3RCtReaxGuV/cfdQjoigtQz80CqoRRbY=','2014-02-14 15:23:34',0,'tholopainen','Tumoas','Holopainen','t.holopainen@nightwish.fi',0,1,'2014-02-14 15:23:34');
INSERT INTO "auth_user" VALUES(24,'pbkdf2_sha256$12000$JMzqzU5sQmIn$jUPDvnQJSDmKyCxWq14ZqjhsRfCBUIL6TECKB9x3sKQ=','2014-02-14 15:24:14',0,'mhietala','Marco','Hietala','m.hietala@nightwish.fi',0,1,'2014-02-14 15:24:14');
INSERT INTO "auth_user" VALUES(25,'pbkdf2_sha256$12000$Sd9mIjQMm9Ko$bbsDU7LWlan1mrpDq1ttw/86XnNm9KFo/O+ZPD96jrk=','2014-02-14 15:24:51',0,'fleone','Fabio','Leone','f.leone@rhapsody.it',0,1,'2014-02-14 15:24:51');
COMMIT;
