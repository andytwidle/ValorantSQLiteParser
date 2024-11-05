class Match_player:
    def __init__(self, matchPlayerId: int, matchId: str, subject: str, gameName: str, tagLine: str, platformInfo: str, teamId: str, partyId: str, characterId: str, score: int, roundsPlayed: int, kills: int, deaths: int, assists: int, playtimeMillis: int, grenadeCasts: int, ability1Casts: int, ability2Casts: int, ultimateCasts: int, roundDamage: str, competitiveTier: int, isObserver: str, playerCard: str, playerTitle: str, preferredLevelBorder: str, accountLevel: int, sessionPlaytimeMinutes: int, afkRounds: int, collisions: str, commsRatingRecovery: int, damageParticipationOutgoing: int, friendlyFireIncoming: int, friendlyFireOutgoing: int, mouseMovement: int, selfDamage: int, stayedInSpawnRounds: int, newPlayerExperienceDetails: str, timeSinceLastMatch: int = None):
        self.matchPlayerId = matchPlayerId
        self.matchId = matchId
        self.subject = subject
        self.gameName = gameName
        self.tagLine = tagLine
        self.platformInfo = platformInfo
        self.teamId = teamId
        self.partyId = partyId
        self.characterId = characterId
        self.score = score
        self.roundsPlayed = roundsPlayed
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.playtimeMillis = playtimeMillis
        self.grenadeCasts = grenadeCasts
        self.ability1Casts = ability1Casts
        self.ability2Casts = ability2Casts
        self.ultimateCasts = ultimateCasts
        self.roundDamage = roundDamage
        self.competitiveTier = competitiveTier
        self.isObserver = isObserver
        self.playerCard = playerCard
        self.playerTitle = playerTitle
        self.preferredLevelBorder = preferredLevelBorder
        self.accountLevel = accountLevel
        self.sessionPlaytimeMinutes = sessionPlaytimeMinutes
        self.afkRounds = afkRounds
        self.collisions = collisions
        self.commsRatingRecovery = commsRatingRecovery
        self.damageParticipationOutgoing = damageParticipationOutgoing
        self.friendlyFireIncoming = friendlyFireIncoming
        self.friendlyFireOutgoing = friendlyFireOutgoing
        self.mouseMovement = mouseMovement
        self.selfDamage = selfDamage
        self.stayedInSpawnRounds = stayedInSpawnRounds
        self.newPlayerExperienceDetails = newPlayerExperienceDetails
        self.timeSinceLastMatch = timeSinceLastMatch

    @classmethod
    def from_row(cls, row):
        return cls(
            row['matchPlayerId'],
            row['matchId'],
            row['subject'],
            row['gameName'],
            row['tagLine'],
            row['platformInfo'],
            row['teamId'],
            row['partyId'],
            row['characterId'],
            row['score'],
            row['roundsPlayed'],
            row['kills'],
            row['deaths'],
            row['assists'],
            row['playtimeMillis'],
            row['grenadeCasts'],
            row['ability1Casts'],
            row['ability2Casts'],
            row['ultimateCasts'],
            row['roundDamage'],
            row['competitiveTier'],
            row['isObserver'],
            row['playerCard'],
            row['playerTitle'],
            row['preferredLevelBorder'],
            row['accountLevel'],
            row['sessionPlaytimeMinutes'],
            row['afkRounds'],
            row['collisions'],
            row['commsRatingRecovery'],
            row['damageParticipationOutgoing'],
            row['friendlyFireIncoming'],
            row['friendlyFireOutgoing'],
            row['mouseMovement'],
            row['selfDamage'],
            row['stayedInSpawnRounds'],
            row['newPlayerExperienceDetails']
        )

class Match_info:
    def __init__(self, matchId: str, mapId: str, gamePodId: str, gameLoopZone: str, gameServerAddress: str, gameVersion: str, gameLengthMillis: int, gameStartMillis: int, provisioningFlowID: str, isCompleted: str, customGameName: str, forcePostProcessing: str, queueID: str, gameMode: str, isRanked: str, isMatchSampled: str, seasonId: str, completionState: str, platformType: str, premierMatchInfo: str, partyRRPenalties: str, shouldMatchDisablePenalties: str):
        self.matchId = matchId
        self.mapId = mapId
        self.gamePodId = gamePodId
        self.gameLoopZone = gameLoopZone
        self.gameServerAddress = gameServerAddress
        self.gameVersion = gameVersion
        self.gameLengthMillis = gameLengthMillis
        self.gameStartMillis = gameStartMillis
        self.provisioningFlowID = provisioningFlowID
        self.isCompleted = isCompleted
        self.customGameName = customGameName
        self.forcePostProcessing = forcePostProcessing
        self.queueID = queueID
        self.gameMode = gameMode
        self.isRanked = isRanked
        self.isMatchSampled = isMatchSampled
        self.seasonId = seasonId
        self.completionState = completionState
        self.platformType = platformType
        self.premierMatchInfo = premierMatchInfo
        self.partyRRPenalties = partyRRPenalties
        self.shouldMatchDisablePenalties = shouldMatchDisablePenalties

    @classmethod
    def from_row(cls, row):
        return cls(
            row['matchId'],
            row['mapId'],
            row['gamePodId'],
            row['gameLoopZone'],
            row['gameServerAddress'],
            row['gameVersion'],
            row['gameLengthMillis'],
            row['gameStartMillis'],
            row['provisioningFlowID'],
            row['isCompleted'],
            row['customGameName'],
            row['forcePostProcessing'],
            row['queueID'],
            row['gameMode'],
            row['isRanked'],
            row['isMatchSampled'],
            row['seasonId'],
            row['completionState'],
            row['platformType'],
            row['premierMatchInfo'],
            row['partyRRPenalties'],
            row['shouldMatchDisablePenalties']
        )

class Match_round:
    def __init__(self, matchRoundId: int, matchId: str, roundNum: int, roundResult: str, roundCeremony: str, winningTeam: str, bombPlanter: str, plantRoundTime: int, plantPlayerLocations: str, plantLocation: str, plantSite: str, defuseRoundTime: int, defusePlayerLocations: str, defuseLocation: str, playerStats: str, roundResultCode: str, playerEconomies: str, playerScores: str, bombDefuser: str):
        self.matchRoundId = matchRoundId
        self.matchId = matchId
        self.roundNum = roundNum
        self.roundResult = roundResult
        self.roundCeremony = roundCeremony
        self.winningTeam = winningTeam
        self.bombPlanter = bombPlanter
        self.plantRoundTime = plantRoundTime
        self.plantPlayerLocations = plantPlayerLocations
        self.plantLocation = plantLocation
        self.plantSite = plantSite
        self.defuseRoundTime = defuseRoundTime
        self.defusePlayerLocations = defusePlayerLocations
        self.defuseLocation = defuseLocation
        self.playerStats = playerStats
        self.roundResultCode = roundResultCode
        self.playerEconomies = playerEconomies
        self.playerScores = playerScores
        self.bombDefuser = bombDefuser

    @classmethod
    def from_row(cls, row):
        return cls(
            row['matchRoundId'],
            row['matchId'],
            row['roundNum'],
            row['roundResult'],
            row['roundCeremony'],
            row['winningTeam'],
            row['bombPlanter'],
            row['plantRoundTime'],
            row['plantPlayerLocations'],
            row['plantLocation'],
            row['plantSite'],
            row['defuseRoundTime'],
            row['defusePlayerLocations'],
            row['defuseLocation'],
            row['playerStats'],
            row['roundResultCode'],
            row['playerEconomies'],
            row['playerScores'],
            row['bombDefuser']
        )