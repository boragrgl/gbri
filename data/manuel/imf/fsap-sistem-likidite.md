# Kaynak Belge: 001-article-A001-en (2).pdf

- Orijinal dosya: 001-article-A001-en (2).pdf
- Toplam sayfa: 36
- Metni çıkarılan sayfa: 35
- Kaynak: IMF PDF

---

## PDF Sayfa 1

INTERNATIONAL MONETARY FUND 4Executive Summary
Structural changes since the Global Financial Crisis (GFC) have fundamentally reshaped financial stability risks.
As NBFIs and market-based finance have become more prominent, systemic liquidity stress—where numerous financial
institutions concurrently experience liquidity shortages—has grown in importance alongside traditional bank-focused
solvency concerns. NBFIs now face heightened market-driven liquidity risks due to leverage, maturity mismatches,
derivatives exposures, and reliance on repo funding. Their close ties to banks further amplify contagion throughout the
financial system. Additionally, post-GFC reforms introducing centralized clearing have often shifted certain solvency risks,
such as counterparty credit risk from defaults, into liquidity risks with the introduction of margining practices. Even in
countries where domestic NBFIs are relatively small, global asset managers can transmit external shocks through volatile
capital flows, linking domestic financial stability risks tightly to external and foreign exchange liquidity conditions. Recent
events—including the “dash for cash” and the 2022 stress episode involving NBFIs with liability-driven investment (LDI)
strategies—demonstrate how liquidity shocks can emerge suddenly and propagate across the interconnected balance
sheets of NBFIs and banks, through mechanisms such as margin and collateral calls, investor redemptions, and fire
sales.
In response, international financial stability groups have increasingly called for systemwide stress testing
approaches that can capture cross-sectoral amplification channels among banks and NBFIs. Traditional stress
testing tools typically focus on vulnerabilities within a single sector—such as banks, insurers, or investment funds—while
contagion analyses are often limited to the banking network due to data availability, or rely on market price-based
systemic risk measures from the academic asset pricing literature. Recognizing these limitations, the Financial Stability
Board (FSB) and various sectoral Standard Setting Bodies (SSBs) have, in recent years, emphasized the importance of
assessing risks and vulnerabilities from a systemwide perspective—encompassing both cross-sectoral and cross-border
amplification channels—to better monitor risks and guide policy decisions. As a result, several national authorities in
advanced economies have begun developing experimental top-down models using available supervisory data, an
approach consistently applied in IMF exercises, while some authorities have been conducting bottom-up exercises in
collaboration with private sector participants.
Despite a robust theoretical foundation, developing systemwide stress testing models is hampered by
significant data, technical, and resource constraints.  Academic research provides extensive insights into the
mechanism of systemic liquidity stress—from bank runs and market dislocations to repo market disruptions and margin
call-induced liquidity pressures. However, limited data availability, particularly for lightly regulated NBFIs, off-balance-
sheet exposures, and cross-border transactions, restricts the scope and depth of these analyses. Accurately capturing
behavioral responses to liquidity shocks remains challenging, as institutional reactions are complex and highly context
dependent. While bottom-up exercises can help address some data gaps, integrating these results consistently across
diverse environments is not straightforward. Moreover, expanding model coverage to include risks from derivatives,
repos, and the positions of lightly regulated NBFIs requires substantial transaction-level data, demanding data
management and coordination across agencies. These factors make comprehensive systemwide modeling both resource
intensive and operationally complex.
Against this backdrop, this paper introduces two generic IMF systemwide analysis tools and their application
and extensive enhancement in FSAP over the past decade. TheIMF began developing these tools nearly a decade
ago, recognizing that a systemwide perspective is crucial for financial stability in small open economies—particularly
emerging market economies, where systemic liquidity risks are closely linked to cross-border FX flows and external
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 2

INTERNATIONAL MONETARY FUND 5stability, both core elements of the IMF mandate. The first is an Excel-based systemwide liquidity analysis tool, leveraging
sector-aggregate flow-of-funds data to monitor liquidity shocks and their transmission across domestic financial linkages.
Importantly, the Excel tool is suitable for a broad range of economies, including some low-income countries, now that
such data have become available for many members. The second tool is the Market Impact from Investment Funds
Liquidity Distress (MILD) framework, which uses granular investment funds and their asset data to assess redemption
pressures, asset sales, and secondary price effects. Both tools are adaptable for FSAPs, tailored to country-specific data
and priorities and often augmented significantly to deliver customized and in -depth analysis.
FSAP applications frequently revealed key vulnerabilities and mitigating factors, and identified critical data gaps
to improve. Initial efforts focused on emerging and developing economies, where external shocks, volatile capital flows,
and FX liquidity constraints drive systemic risk. Often, nonfinancial entities—corporates, households, or the public
sector—played major roles in transmitting or triggering systemic liquidity stress. Later FSAPs broadened systemwide
analysis to advanced financial systems, integrating various NBFI segments, fire-sale price effects, and, more recently,
liquidity needs from repos and derivatives based on transaction-level data. Advanced economies’ cases showed that
liquidity stress can rapidly spread across banks, insurers, money market funds, and core funding markets—even without
significant solvency losses. In contrast with most national authorities’ exercises, FSAP analyses usually explored a range
of behavioral scenarios to identify the actors and actions most likely to drive or mitigate systemic risk instead of choosing
specific ones. Moreover, most exercises carefully discussed the systemwide consistency of clients’ money withdrawals or
redemptions from financial institutions. Whether they stay in the domestic system or exit the country determines the
systemic impact through macroeconomic channels involving exchange rate and capital flows—a feature that national
authorities’ exercises typically do not account for.
Drawing on these experiences, this paper highlights future priorities for advancing systemwide stress testing at
the IMF. Progress in the near term depends on leveraging currently available, but often underutilized, data reported to
national regulators—such as banks’ granular counterparty credit and large exposure information—to better measure
linkages with NBFIs and identify potential risk concentrations. Another key area is deeper integration of market
microstructure, margining, and clearing arrangements into stress scenarios by utilizing transaction-level data collected by
financial market infrastructures (FMIs), as demonstrated in the 2025 Euro Area FSAP. Because managing these data is
resource-intensive and confidentiality provisions often exceed those for standard macro scenario stress tests, close
collaboration with national authorities and, ideally, key FMIs is crucial. Over time, insights from bottom-up exercises and
behavioral evidence can support more sophisticated behavioral modeling approaches, including agent-based
frameworks. Continued international efforts to address data gaps will help illuminate dark corner of finance and more
systematic data-sharing and coordination across national authorities could facilitate better use of existing data sources.
Overall, systemwide stress testing represents a valuable addition to the financial stability toolkit despite its
current limitations.  While not designed to deliver precise assessments of system resilience, these exercises are
effective in identifying potential weak links, critical data gaps, policy trade-offs, and regulatory features that may
strengthen individual sectors while increasing system-wide fragility. As financial systems continue to evolve toward
greater market-based intermediation, systemwide approaches will remain central to understanding and mitigating
systemic risks.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 3

INTERNATIONAL MONETARY FUND 6Introduction
The Rising Prominence of Nonbank Financial Institutions
The financial sector has changed markedly since the Global Financial Crisis (GFC), with nonbank financial
institutions (NBFIs)—especially asset managers—assuming a far more important role (Figure 1).  Of over $500
trillion in global financial assets, NBFIs now hold $256 trillion (FSB, 2025). While NBFIs have traditionally made up about
half of total system assets, banks’ share has gradually receded since the GFC. NBFIs are typically larger in advanced
economies, whereas banks still prevail in most emerging and developing economies, though there are significant
jurisdictional differences. Notably, structural changes within the NBFI sector have accelerated: “other financial institutions”
(OFIs)—NBFIs excluding pension funds, insurers, and financial auxiliaries as categorized by the Financial Stability Board
(FSB)—have rapidly expanded, propelled by the asset management industry, which includes money market funds
(MMFs), hedge funds, and other investment vehicles.1 The rise of NBFIs has also shifted the focus of short-term funding
markets away from unsecured interbank lending and toward sovereign repos and derivatives, which are accessible by
banks and NBFIs alike (Pinter and Walker, 2023; Alfaro and others, 2024).
NBFIs, and the asset management industry in particular, face significant market risks from their activities in
money and capital markets, which can result in liquidity stress.  Most invest in marketable securities, and many
pursue higher yields via derivatives, repos, and synthetic instruments. Some of them, particularly hedge funds and private
family offices, are highly leveraged with direct borrowing from banks or with synthetic instruments. Open-end funds are
especially susceptible to liquidity stress: declines in net asset values (NAVs) can prompt large client redemptions, forcing
managers to run down cash buffers or fire sale assets—a “dash-for-cash”—especially when investment strategies have
maturity or liquidity mismatches.2 Even without redemptions, funds with derivatives or repo exposures may face urgent
collateral or cash needs due to margin calls. Simultaneously, ongoing structural changes in the insurance and pension
sectors including increasing integration with the asset management industry, have made the sector more exposed to
shocks.3 Their search for yield has led them into alternative assets and more short-term investments in derivatives and
repos, heightening their exposure to liquidity risk—such as seen in the 2022 stresses affecting UK pension funds with
liability-driven investment (LDI) strategies.4
1 An OFI is a subset of NBFIs that excludes insurers, pension funds, and financial auxiliaries, and includes money market funds (MMFs), hedge
funds, other investment funds, captive financial institutions, money lenders, central counterparties (CCPs), broker-dealers, financial
companies, trust companies, and structured finance vehicles. In this paper, “asset management industry” refers to the sum of MMFs, hedge
funds, and other investment funds. Financial auxiliaries are entities that provide services that enable financial transactions, markets, or
institutions to function but do not engage in bank -like activities such as leverage or maturity transformation and are composed for example of
Brokerage firms or credit rating agencies
2 The market turbulence and resulting liquidity stress may push some asset management funds to default on their short-term financial contracts
(i.e., counterparty credit risk), but not necessarily to insolvency, namely negative capital. Investment funds’ losses are absorbed by funds’
shareholders, unless they are leveraged and fall into insolvency.
3 Life insurers are shifting investments from traditional bonds and equities to alternative assets such as private equity, heightening risks from
leverage, liquidity mismatches, and uncertain valuations. In some jurisdictions, private equity firms have bought insurers increasing cross-
sectoral interconnectedness (IMF, 2023). New business models have enabled life insurers (through asset intensive reinsurance exploiting
regulatory arbitrage opportunities, IAIS 2025 ) and property and casualty insurers (through catastrophe bonds, IAIS 2023  and IAIS and the
World Bank 2025 ) to transfer risk to broader markets and across borders, diversifying risks, but also increasing interconnectedness.
4 LDI funds had extensively used repo to borrow cash and buy gilts to increase their leverage. This generated large collateral calls, on top of
margin calls from derivative positions such as interest rate swaps. LDI funds and pension funds had mainly long-term gilts, a market with
limited depth, which amplified the price impact of the large sales of gilts. It generated a self-reinforcing spiral that that threatened the
functioning of core UK funding markets, forcing the Bank of England to intervene (Cunliffe, 2022, Chen and Kemp, 2023).
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 4

INTERNATIONAL MONETARY FUND 7Figure 1. Global Financial System Landscape
Over the past two decades, the shares of NBFIs and banks remained
broadly constant.The global picture masks substantial differences across countries.
Among NBFIs, the asset management segment grew significantly in
the total global financial system……and among “bank-like” NBFIs.
Moreover, the asset management segment further increased its
footprint in key off-balance-sheet derivatives not reflected in size
indicators……and repo markets, many of which have become benchmark rate
markets around 2023, replacing LIBOR and other interbank offer
rates.2
Sources: FSB NBFI Monitoring Report ( 2025a), FSB Vulnerabilities in Government Bond-backed Repo Markets ( 2026), and staff calculation.
1 The percentage of OFI assets to GDP for the Cayman Islands (287,381), Luxembourg (20,854), Ireland (1,480) and the Netherlands (544) are not shown
since they are particularly high compared to the rest of the jurisdictions.
2 LIBOR and other interbank offer rates were previously used as benchmark rates for pricing financial contracts. Following concerns about these markets,
G7 central banks adopted new benchmark rates based on repos or interest rate swaps that reflect NBFI trading activity (see FSB, “Goodbye Libor, hello
basis traders,” 2025 ).
3Outstanding amounts, reported by FSB members.
4651
233442 38
0102030405060
010020030040050060070020022003200420052006200720082009201020112012201320142015201620172018201920202021202220232024
Central bank
 Public financial institutions
Bank
 Pension, insurance, axilliaries
OFI-asset management
 OFI-others
Share of NBFI, rhs Share of OFI, rhs
Share of Bank, rhsEvolution of Global Financial System: G29, 2002-24
(Left scale, assets in USD trillion; right scale, share in percent of total)
0100200300400
020406080100HKFRSGESDEUKJPBEKRITAUCACHNLUSIELUKYSACNTRIDINARBRCLMXZAAllAEsEMEs
Banks
 Central banks
Public financial institutions
 Insurance corporations
Pension funds
 Financial auxiliaries
OFIs OFI as percentage of GDP (rhs) 1/The Structure of financial System by Jurisdication, 2024
(Left scale = assets in percent of total, right scale = in percent of GDP)
3957
010203040506070
02040608010012014016018020022003200420052006200720082009201020112012201320142015201620172018201920202021202220232024
MMFs
 Hedge Funds
Other investment funds
 Broker dealers
Structured finance
 Others
Share of asset management, rhsOther Financial Institution: G29, 2002-24
(Left scale, assets in USD trillion; right scale, in percent of total OFI assets)
Share of asset mananagement
(MMF, hedge funds, other
investment funds)
4244485358626669717475 76 757778 7876 7678
0102030405060708090
2006
2007
2008
2009
2010
20112012
2013
2014
2015
2016
2017
2018
2019
20202021
2022
2023
2024Asset managers
Finance companies
Broker dealers
Credit insurance
SecuritizationStructure of NBFIs Engaging in Credit Intermediation
(In percent of total assets held by "bank-like" NBFIs)
-0.500.5
2010 2015 2020 2025Asset managers Dealer intermediary Leveraged funds
S&P 500Net Treasury and Equity Futures Positions
(Trillions of dollars)
-1.5-1-0.500.511.5
2010 2015 2020 2025US Treasuries
Triparty (1%) , inter-dealerLargely an inter-dealer or
inter-bank, but is also
used for transactions
between dealers/banks
and NBFIsOften involves dealers/banks and NBFIs
Mostly money market funds and pension funds
lending to intermediaries.Triparty (16%)Centrally cleared Not centrally cleared
Bilateral (32%) Bilateral (50%)Aggregate breakdown of main repo markets segments across
jurisdictions (2024) 3/
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 5

INTERNATIONAL MONETARY FUND 8The Need for a Systemwide Perspective
As a result, systemic liquidity stress—sparked by sharp market shocks and amplified by NBFIs and their
interconnectedness with banks—has become a core concern for financial stability . Systemic liquidity events arise
when numerous institutions experience liquidity strains at once (IMF 2011; ECB 2018). Market valuation shocks may
trigger liquidity stress for entities directly exposed to these assets, while also propagate to other entities due to
interconnections. For example, major shifts in global monetary policy, as in 2022, can have significant impacts on NBFIs
and banks (as seen in the 2023 banking turmoil). The resulting dash-for-cash may further magnify market shocks and
transmit or amplify liquidity stress across the financial system, extending beyond simple fire sales and common
exposures due to cash or additional collateral needs from margin calls (Duffie and others 2015; Czech and others,
2021).5 For instance, the sudden collapse of Archegos in 2021 illustrates how margin calls on unregulated family
investment offices can inflict more than $10bn in losses on banks via leveraged, concentrated, and opaque investments
(Bouveret and Haferkorn, 2023). Likewise, in early 2025, trade tensions caused large swings in equity, bond, and
commodity markets, leading to significant margin calls. Such shocks can be amplified through leverage (including off-
balance-sheet contracts), counterparty credit risk (defaults on contracts, with or without insolvency, often stemming from
liquidity distress), and funding risk (where entities lose access to funding from distressed counterparties), affecting both
banks and other NBFIs.
Cross-exposures between NBFIs and banks are widespread, especially in advanced economies (AEs, Figure 2).
All types of NBFIs are globally interconnected with banks, each other, and across borders. The link between NBFIs and
banks has grown, becoming systemic for banks in the US and Europe, where some large institutions have NBFI
exposures exceeding their Tier 1 capital. However, the nature of these linkages varies by NBFI segment; notably, hedge
funds often exhibit pronounced cross-border connections due to their prevalent domiciliation in favorable tax regimes.
Flow-of-funds statistics (Figure 2), based on the System of National Accounts (SNA), reflect only balance sheet
linkages—the true extent of interconnectedness may be greater once off-balance-sheet exposures, including derivatives,
are included.
Even where domestic NBFIs remain small, as in many emerging and developing economies (EMDEs), the global
asset management industry can still contribute to systemic risks.  Portfolio investments into EMDEs are often
channeled by global asset managers, transmitting global liquidity cycles into recipient economies. How these flows move
upon global shocks depends on the structure of the investor base and asset types (Brandao-Marques and others 2022).
Shocks to capital flows often hit equity and bond markets first, then ripple through the domestic financial system via local
dash-for-cash behavior, impacting asset prices and exchange rates. Depending on the country’s international investment
position, systemic liquidity stress may originate in nonfinancial corporates (NFCs) and government sectors—which tend to
rely more on foreign funding when domestic capital markets are underdeveloped—as well as in financial institutions.
Ultimately, these shocks tend to result in liquidity shortfalls within domestic financial institutions via local financial
linkages.
5 Margins are collected to compensate for potential credit losses when a counterparty cannot honor contracts. Margin amount is continuously
adjusted, and sudden large market movements could create additional margin calls—typically in cash or highly liquid assets—at short notice,
resulting in liquidity risks.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 6

INTERNATIONAL MONETARY FUND 9Figure 2. NBFI and Interconnectedness
Banks and NBFIs are closely interconnected through common
exposures to sovereign debt within and across borders. Linkage between NBFIs and banks has become
substantial for banks. In the United States, banks
representing almost 50 percent of banking system assets
have exposures to NBFIs exceeding their Tier 1 capital,
and these links may increase both solvency and liquidity
risks in the banking sector.
Globally, all types of NBFIs are interconnected with banks,
among themselves, and across-borders.The patterns of interconnections (asset side, liability side)
differ across different segments of NBFIs—Cross-border
linkage of hedge funds stands out as many of them are
domiciled in financial centers with beneficial tax regimes.
Sources: Arslanalp and Tsuda (2014), data updated; FSB ( 2025a ), IMF October 2025 GFSR, IMF staff estimates.
Notes: The abbreviations stand for: Insurance corporations (ICs), Pension funds (PFs), Financial auxiliaries (FAs), Households
(HHs), non-financial companies (NFCs). CBs include CBs and PFIs and nonbank DTCs. Unspecified indicates linkages to other
sectors not identified by jurisdiction or type of institutions not defined above. The following types of OFIs are included: MMF =
money market funds; HFs = hedge funds; OIFs = other investment funds; FIFs = fixed income funds; FinCos = finance
companies; SFVs = structured finance vehicles.
More generally, when cross-border capital flows are systemically important, financial stability risks become
closely tied to external stability risks—especially the exchange rates and the adequacy of international reserves.
Large capital outflows from EMDEs and small open economies without a reserve currency raise demand for hard-
currency foreign exchange (FX) liquidity. Even when foreign investors hold assets denominated in local currency and
bear currency risks, their exits can cause a surge in FX liquidity needs as they repatriate funds in hard currencies.
Domestic investors can also trigger capital outflows and demand for FX by reallocating assets abroad or into hard
currencies (cash under the mattress or in stablecoins and other crypto assets). FX demand spikes can lead to bank FX
0%10%20%30%40%50%60%70%80%90%100%
Canada France Germany Italy Japan United
KingdomUnited
States
Domestic central bank
 Domestic banks
 Domestic nonbanks
Foreign official
 Foreign banks
 Foreign nonbanksInvestor Base of G7 General Government Debt, 2025Q2
(In percent)
Sources: Arslanalp and Tsuda (2014, updated)0100200300400500600Total NBFI Exposure to Tier 1 Capital
Total NBFI Loans to Tier 1 Capital
United States                                                               Euro Area
Banks rated from highest to lowest NBFI exposure concentrationBanks' NBFI Exposure to Tier 1 Capital
(Percent)
0 20 40 60 80 100ClaimsLiabilitiesClaimsLiabilitiesClaimsLiabilitiesClaimsLiabilitiesBanks OFIs ICs PFs
Banks
 OFIs ICs PFs
FAs HHs NFCs CBs
Gov RoW UnspecifiedAggregated linkages by institution type
(In percent of total financial assets)
020406080100ClaimsLiabilities Claims Liabilities ClaimsLiabilitiesClaims Liabilities ClaimsLiabilitiesClaims Liabilities Claims Liabilities
MMFs HFs OIFs FIFs FinCos BDs SFVs
Banks
 OFIs
 ICs
 PFs
 HHs
 NFCs
 Gov
 RoW
 Unspecified²Identified OFI linkages with other financial market
participants (In percent of entity's total assets)
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 7

INTERNATIONAL MONETARY FUND 10shortages or sharp currency depreciation. Unlike shortages in local currency liquidity, systemic FX gaps are challenging
for central banks to manage, as their firepower to provide FX liquidity support is generally limited to international reserves.
Thus, central bank and government financial accounts become crucial in systemwide analysis in these scenarios. In fact,
incorporating financial stability–related reserve adequacy discussion has become a key part of the IMF’s external stability
work (IMF, 2014a and 2016).
Given the crucial role of inter-sectoral interconnectedness in propagating systemic liquidity shocks, there is a
need for “systemwide” analysis to understand how such crises unfold . A systemwide analysis is defined as an
interconnectedness exercise considering multiple key sectors, capturing both direct (through cross-exposures) and
indirect (through common exposures, firesale price dynamics, and margin calls) contagion effects among them.6 The IMF
has been experimenting with systemwide liquidity analysis for nearly a decade in FSAPs and technical assistance work.
They are bilateral exercises often using confidential country-specific data and tailored to each jurisdiction and cover broad
sectors, including nonfinancial sectors when relevant, and IMF membership with cross-country perspectives. These
exercises complement global vulnerability assessments, international standard-setting and policy work, and national
exercises, by tracing how identified vulnerabilities may propagate across sectors and borders and interact with broader
macroeconomic and external stability risks. These efforts resonate with similar calls by the FSB for systemwide
approaches to NBFI risk (FSB, 2020), the ESRB High-Level Group’s recommendation to use systemwide stress testing
(ESRB, 2024), and initiatives by national authorities like the Bank of England’s (BoE’s) System-Wide Exploratory
Scenario (SWES)—a “bottom-up,” systemwide exercise with broad private sector involvement (BoE, 2024). The rest of
the introduction section reviews the theoretical foundations of systemic liquidity crises and operational models for
assessing liquidity risk in both sector-specific and systemwide settings, highlighting the IMF’s contributions to date.
Literature
Theory
The academic literature on the theory of systemic liquidity crises is extensive and well-developed. Early theories
of banking and financial crises, rooted in historical bank run experiences, began with Diamond and Dybvig (1983), who
analyzed idiosyncratic bank runs. Subsequent research by Allen and Gale (1998, 2000, 2004), Morris and Shin (1998),
Holmstrom and Tirole (1998, 2011), Freixas, Parigi, and Rochet (2000), and Rochet and Vives (2004) expanded the focus
to systemic runs affecting the broader banking system. These studies emphasize that systemic runs typically arise from
economy-wide stress—such as recessions—and behaviors that amplify minor shocks into full-scale crises due to
heightened uncertainty.
Post-GFC research has substantially advanced the understanding of how isolated shocks can escalate into
systemic crises through multiple amplification channels in financial markets.  The growth of securitization—
particularly mortgage-backed securities—combined with real estate booms, heightened banks’ exposures to market
instruments and increased their reliance on collateralized wholesale funding. These shifts in business models introduced
new amplification mechanisms, including “run on repos” and collateral channels (Gorton and Metrick, 2012), fire sales
6 In this paper, second-round effects refer to feedback generated by institutions’ responses to an initial shock. For example, liquidity-driven asset
sales may depress market prices, further increasing valuation losses, redemptions, margin or collateral calls, and asset sales. FSAP
analyses endogenize selected feedback channels relevant to the exercise but generally remain scenario-based, partial-equilibrium
assessments rather than general-equilibrium models in which prices, quantities, behaviors, macroeconomic conditions, and policy responses
are jointly determined.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 8

INTERNATIONAL MONETARY FUND 11(Shleifer and Vishny, 2011), the interplay between market and funding liquidity (Brunnermeier and Pedersen, 2008),
leverage cycles (Adrian and Shin, 2010), and cash hoarding fueled by uncertainty and network effects (Allen and Gale,
2004; Allen, Carletti, and Gale, 2009; Gai, Haldane, and Kapadia, 2011; Anand, Gai, and Marsili, 2012; Diamond and
Rajan, 2011).
More recent systemic liquidity events, often triggered or amplified by margin and collateral calls, have further
enriched the literature.  Bakoush, Gerding, and Wolfe (2019) employed an agent-based network model to link margin
procyclicality with interbank liquidity hoarding, highlighting spillovers from margin call stress in derivative markets into
interbank markets. Their work also demonstrated how central clearing and tighter haircuts can increase fragility, while the
central bank’s market-maker-of-last-resort function can mitigate stress. Aramonte, Schrimpf, and Shin (2023) showed,
using a stylized accounting framework, that margin increases can sharply reduce debt-taking capacity under widespread
collateralized borrowing, triggering deleveraging and dash-for-cash dynamics, also shared with the FSB (2024a). King
and others (2020) conceptualized central clearing counterparties (CCPs) as liquidity transformers, noting significant
variation and opacity in margin practices across CCPs (BCBS, CPMI and IOSCO, 2022).
Empirical and Operational Risk Assessment
The application of these theories to financial stability risk assessment depends on data availability (Table 1).
Regulators collect granular, institution-based confidential data for banks and insurers, while security-level asset holdings,
NAV, and inflows/redemption data are publicly available for investor protection in publicly offered investment funds.
However, supervisory or publicly available data are sparse for alternative asset managers such as hedge funds and
private family offices—the dark corner of finance. Supervisors of financial market infrastructures (FMIs) often collect
transaction-level data and stress test the resilience of CCPs. Activity-based analysis—using transaction or deal-level data
for systemwide stability—remains limited, and market price-based academic approaches have gained little traction as
stress testing tools with national authorities as they are too high-levels and noisy.
Significant progress has been made in modeling systemic liquidity and contagion risks within the banking
sector, supported by rich data.7 Numerous operational models now incorporate contagion effects using actual
supervisory data, such as interbank matrices of claims and liabilities (Baranova and others, 2017; Sydow and others,
2024). These models typically overlay contagion channels with conventional solvency or liquidity stress tests. Contagion
can be directly transmitted via counterparty credit risks through bilateral contracts—using network approaches pioneered
by Eisenberg and Noe (2001) and applied by Espinoza-Vega and Sole (2010), Cont, Kotlicki, and Valderrama (2020),
Bargigli and others 2015; and Covi, Gorpe, and Kok (2021)—or indirectly through common exposures (Greenwood and
others, 2015; Cont and Schaanning, 2017; Duarte and Eisenbach, 2021; Coen, Lepore, and Schaanning, 2019; Bidder
and others, 2024) and collateral and liquidation-price dynamics (Gai, Haldane, and Kapadia, 2011).
In the NBFI sector, systemic liquidity risk analysis is primarily centered on open-end mutual funds and, to a
lesser extent, CCPs.  Stress test methodologies for mutual funds have converged internationally, with Bouveret (2017),
Lô and Carpantier (2023), Fricke and Wilke (2023), Gourdel and Sydow (2023), Cetorelli, Landoni, and Lu (2023), and
recent FSAP exercises adopting a common structure: (1) market shocks reduce fund NAVs, (2) redemptions rise
(especially for funds with greater NAV declines), and (3) asset sales drive price impacts, leading to further NAV
reductions through second-round effects. Network approaches are seldom applied due to limited direct cross-holdings,
except among funds of funds. Supervisory stress tests for CCPs focus on short-term market stress scenarios, evaluating
7 See the recent survey by Aikman and others (2022) for details.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 9

INTERNATIONAL MONETARY FUND 12liquidity and solvency resilience of CCPs upon members’ default on contracts (ESMA 2023; BoE 2023; BCBS-IOSCO
2018). However, these exercises usually do not test the resilience of the system including their members and clients who
could be taking risky leveraged positions.8 Recent work by Grippa, Letizia, and Viollet (forthcoming) provides a framework
for assessing the market and counterparty risks generated by CCPs investments. Pension funds and insurers are mainly
assessed for solvency risk from insurance and investment risks, as early withdrawal risk is much less important than for
investment funds. Short-term liquidity stress testing from margin calls is not yet prevalent.
Table 1. Regulatory Data Gaps for NBFIs
NBFIFinancial
leverageLiquidity InterconnectednessCurrency
mismatch
Investment funds
(excluding money
market funds and
hedge funds)
($58 trillion, 12% of
GFA)
Insurance
companies
($40 trillion, 9% of
GFA)
Pension funds
($43 trillion, 9% of
GFA)
Money market funds
($8.5 trillion, 2% of
GFA)N/A N/A
Structured finance
vehicles
($6 trillion, 1% of GFA)
Hedge funds
($6 trillion, 1% of GFA)
Central
counterparties
($0.7 trillion, 0.1% of
GFA)N/A N/A
Sources: IMF, April 2023 GFSR
Note: Red denotes no/very little data in areas with high or medium/high vulnerabilities; orange denotes no/very little data in areas with
low/medium vulnerabilities; yellow denotes some data in select jurisdictions in areas with high or medium/high vulnerabilities; light green denotes
some data in select jurisdictions in areas with low or medium vulnerabilities; dark green denotes broadly adequate data irrespective of level of
vulnerabilities. GFA = global financial assets; N/A = not applicable; NBFI = nonbank financial intermediary.
The Development of Systemwide Exercises
The IMF has been developing and applying a systemwide liquidity analysis in FSAPs and technical assistance
projects for nearly a decade.  These exercises generally apply top-down, scenario-based approaches tailored to
jurisdiction-specific vulnerabilities and available data, estimating liquidity needs and mitigating actions across relevant
8 An exception is Bank of England’s 2025 CCP stress testing exercise  (see its speech as well). The assessment of CCP in the 2021 US FSAP
highlighted the importance of undertaking CCP stress tests with systemwide-focus, in addition to assessing the resilience of CCPs.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 10

INTERNATIONAL MONETARY FUND 13sectors and tracing direct and indirect spillovers under alternative behavioral assumptions.9 Early efforts focused on
EMDEs, where cross-border capital flows via global banks and NBFIs acted as key catalysts for systemic liquidity stress,
transmitting shocks through the interconnected domestic financial system. In these economies, in addition to financial
institutions, government, central banks, and nonfinancial corporations often played critical roles in amplifying external
shocks within the local system. Initial work in AEs examined specific linkages—such as direct connections between banks
and investment funds through deposits—and mapped the system by analyzing common or cross-securities holdings
among banks, investment funds, and insurers. More recent FSAPs have pioneered comprehensive approaches that
integrate liquidity stress across banks, investment funds, and insurers, including the liquidity demands arising from margin
calls on derivatives and repos, and the spillover effects to financial markets through asset fire sales and price impact
dynamics. Between 2020-25, 19 FSAPs have employed some form of systemwide risk analysis (see Annex I).
Systemwide analysis that integrates multiple financial actors is emerging recently among national authorities as
well. They experiment with a range of approaches, each offering complementary perspectives on different dimensions of
systemic risk, as well as with distinct strengths and limitations (Table 2). These analyses rely on balance -sheet
information and focus on cross- exposures and common exposures. Such approaches tend to have greater traction with
financial regulators and institutions than correlation - or dependence -based indicators, which are more closely aligned with
the definition of systemic risk in the asset pricing literature.10
Bottom-up approach with private sector participation:  The Bank of England’s SWES exercise broadens the focus
to core financial markets and their main participants, including banks, insurers, CCPs, hedge funds, pension funds,
and asset managers, to assess collective amplification of shocks (BoE, 2024). It relies heavily on input from private
sector participants to identify critical behavioral patterns influencing shock amplification. This approach, also adopted
by France and Australia, helps address data gaps and improves understanding of behavioral dynamics, though there
are challenges in ensuring systemwide consistency, especially regarding the general equilibrium effects (they usually
cannot go further than second rounds given the need for inputs from participants). These exercises also rely critically
on the cooperation of participating institutions and, where necessary, on collaboration among supervisory authorities
to ensure comprehensive sectoral coverage.
Top-down/desktop approach using supervisory data:  The European Central Bank (Sydow and others, 2024) and
Bank of Canada (BoC) have developed comprehensive models that incorporate market and NBFI risks into macro
scenario-based bank solvency stress tests. In contrast, the Fund, Japan, and Mexico have focused on short-term
systemic liquidity stress scenarios. The Bank of Japan’s framework (Konaka, Murayama, and Nakamura, 2025)
uniquely incorporates foreign investment funds outside domestic regulatory perimeters using public disclosure data.
A recurring challenge is the estimation of price impacts associated with fire sales, underscoring the need for robust
sensitivity analyses and systematic cross-checks using alternative assumptions or modeling approaches. The
trade-off between model complexity and tractability, together with the difficulty of accurately capturing heterogeneous
sectoral behavior under stress, further complicates model design. As a result, these modeling frameworks typically
require substantial analytical and operational resources to develop and maintain.
9 While their design follows broad stress-testing principles, the specification and calibration of shocks are adapted to the circumstances and
analytical priorities of each FSAP
10 See for example Adrian and Brunnermeier (2016) for CoVaR or Acharya and others (2017) for the Marginal Expected Shortfall.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 11

INTERNATIONAL MONETARY FUND 14Table 2. Comparison of top-down vs bottom-up approach
Dimension Top-down systemwide analysis Bottom-up systemwide analysis
ObjectiveIdentify systemwide linkages and amplification
channelsUnderstand behaviors and interactions under
stress
Data &
inputsSupervisory, balance-sheet, flow-of-funds,
transaction dataFirm submissions, market intelligence,
supervisory dialogue
StrengthsSystemwide consistency, scalable across
countriesRealistic behavior, reveals expectation
mismatches
LimitationsResource-intensive for the institution, data gaps,
stylized behavior,Resource-intensive for the institution and the
participants, partial system coverage
ExamplesECB: ISA model
Bank of Canada, Bank of Japan…
All IMF FSAP exercisesBoE: SWES
Banque de France, Reserve Bank of Australia
Source: IMF
Against this backdrop, this paper presents the IMF’s systemwide risk analysis tools, their application, and
notable extensions in FSAPs.  Section II introduces two core tools: an Excel-based tool leveraging sector-aggregate
flow-of-funds data for high-level analysis of systemic interlinkages and transmission channels, and an online dashboard
for investment fund liquidity stress tests that incorporate second-round price effects from asset fire sales. Together, they
illustrate how parsimonious, top -down tools can help identify key amplification channels, systemic sectors, market
spillovers, and data gaps, including where granular data are limited. They also support more coherent interpretation of
sectoral stress tests and provide an operational basis for policy discussions on liquidity regulation, risk management, and
backstops and priorities for further analytical deepening. Section III details notable FSAP applications and refinements in
selected advanced and emerging economies, and the final section concludes.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 12

INTERNATIONAL MONETARY FUND 15IMF’s Generic Systemwide Analysis Models
IMF currently maintains two standardized systemwide analysis tools . The first one is Excel-based systemwide
liquidity analysis tool using sector-aggregate flow-of-funds by counterpart (Oura 2022)—alternatively referred as Balance
Sheet Approach (BSA) data by the IMF (IMF 2015, Harutyunyan and Munoz, 2018). The other is Market Impact from
Investment Funds Liquidity Distress (MILD) by Letizia and Zhang (forthcoming). This approach uses detailed investment
fund data, including their security-level investment, and considers how redemption-driven asset sales affect market prices
and transmit investment fund liquidity stress to financial markets. FSAPs often take these tools as benchmark and tailor
or enhance them as deemed adequate in each assessment and depending on available data.
Excel-Based Systemwide Liquidity Analysis Tool
The Excel-based systemwide liquidity stress testing tool offers a high-level assessment of how aggregate
liquidity shocks affect the economy through domestic financial linkages . These shocks—such as capital outflows,
or shifts from domestic financial assets to commodities (like gold), real assets, and foreign-issued crypto assets—often
manifest as major asset price disruptions, which then propagate through direct financial exposures among entities. The
tool utilizes flow-of-funds data that detail financial assets and liabilities by sector, counterparty, and instrument. Thanks to
the G20 data gap initiative11 and IMF technical assistance, such data are now available for many IMF member countries,
including some low-income economies. This enables systemwide analysis even when granular data are scarce, providing
a foundation for identifying key interlinkages that may require deeper investigation with advanced methods.
Methodologically, the tool runs cash-flow-based liquidity stress tests across systemically important sectors,
ensuring consistency in cross-sectoral flows.  Within a whole financial system, every agent’s asset is another’s
liability—for example, if an investment fund under redemption pressure withdraws deposits from a bank, the liquidity
stress shifts to the bank (Figure 3). This means that resilience in one sector can directly create challenges for another,
even if the originating sector passes its own stress test. Only integrated systemwide exercises, combining liquidity stress
tests across sectors, can accurately evaluate the financial system’s resilience. The ultimate outcome also depends on
how redeemed funds are reinvested: if moved from investment funds to banks, overall system liquidity may be preserved;
if shifted to assets outside the domestic system (e.g., gold or foreign stablecoins), liquidity leaves the domestic market,
possibly triggering second-round effects like exchange rate depreciation.12  As with any systemwide analysis, results are
sensitive to behavioral assumptions—especially regarding the order in which sectors liquidate assets—so the tool
stresses the importance of multiple scenario and sensitivity analyses rather than reliance on a single assumption.
11 The initiative  began in 2009, completed its second phase in 2022, and is expected to begin its third phase, with continued annual monitoring.
The recent progress report (FSB-IMF, 2022) stated that challenges remained in securities financing transaction data, securities statistics,
sectoral accounts, and cross-border exposures of nonbank corporations, among others.
12 Such second-round effects are not part of the Excel-based too, but a separate module can be easily added to incorporate such effects
following, for example, the approach in MILD.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 13

INTERNATIONAL MONETARY FUND 16Figure 3. Domestic Propagation of Balance-of-Payment Shocks: Example—Banks and
Investment Funds
Source: Oura, 2022
The tool is especially effective in analyzing the interplay between financial system stability and external
vulnerability.  Systemwide liquidity loss can originate from capital outflows or domestic shocks that prompt both domestic
and foreign investors to shift assets abroad, transmitting stress through interconnected sectors. This dynamic often
serves as a primary channel for stress amplification in many EMDEs and small open AEs without a reserve currency.
When such shocks strains key financial institutions and markets, central banks may provide liquidity backstops to avert a
systemic crisis. However, if liquidity stress is driven by capital flows, it results in FX liquidity outflows, regardless of the
level of dollarization.13 Consequently, the central bank’s capacity to respond—whether through FX liquidity support to
financial institutions or direct FX market intervention—is ultimately limited by the level of international reserves. This
underscores the IMF’s (IMF, 2014a, 2016, 2022a) call for tailored analytical frameworks for AEs that explicitly link
financial stability risks with assessments of external stability in IMF country surveillance.
13 If investors are switching from local currency denominated domestic assets to foreign assets, FX demand occurs when investors exchange
sales proceeds (in local currency) for foreign currency to purchase foreign assets.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 14

INTERNATIONAL MONETARY FUND 17Market Impact from Investment Funds Liquidity Distress (MILD)
MILD aims to provide a structured and operational way to assess liquidity vulnerabilities in the investment fund
sector and the systemic spillovers to financial markets from funds.  It is motivated by the structural liquidity mismatch
of open- ended funds, which offer frequent redemptions while holding assets that may be costly to liquidate under stress.
MILD goes beyond a narrow investment fund stress test that examines fund-level resilience against redemptions (first-
round effects) and investigates the second-round effects from funds’ distress—namely, how asset price markets are
disrupted as funds under redemption stress liquidate their potentially illiquid assets. Within the IMF, an internal dashboard
is linked to global investment funds and securities price data and delivers timely analytical outputs with little additional
costs, supporting regular financial surveillance and FSAPs.
The model has similar structures to the approaches developed by national authorities, which have converged
over time, as discussed in the literature review.  It is a modular, scenario -based stress testing framework built on
highly granular fund - and asset -level data (Figure 4). It combines (i) redemption shocks calibrated using parametric
assumptions, historical flows, or estimated flow- performance relationships; (ii) optional market shocks applied to asset
valuations; and (iii) detailed modeling of asset liquidity, liquidation pecking orders, and mitigating actions such as short-
term repo borrowing. Funds’ liquidity demand is translated into asset sales under alternative behavioral assumptions
(e.g., waterfall, pro -rata, or mixed strategies), after which market impact functions map sales volumes into price declines
for specific asset segments. The resulting outputs—liquidity shortfalls, assets sold, market price impact, and losses to
funds and other sectors—are presented as distributions and ranges across scenarios and assumptions, making MILD
particularly useful for systemwide risk identification, sensitivity analysis, and policy discussions on fund behavior and
market resilience.
Figure 4. Stylized Representation of the Framework
Source: Letizia and Zhang, forthcoming
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 15

INTERNATIONAL MONETARY FUND 18However, MILD is not designed to ensure full systemwide consistency or capture all feedback effects and also
face limitations similar to other systemwide tools.  As a partial-equilibrium framework, it does not model general-
equilibrium dynamics, strategic interactions among all market participants, or endogenous policy responses from central
banks or treasuries. Unlike the Excel-based systemwide liquidity tool, MILD does not track how redeemed funds are
reinvested, and instead focus on incorporating the direct second-round effects. Results hinge on behavioral assumptions
and parameter choices—especially for redemption patterns, liquidation strategies, and market depth (volatility and trading
volumes)—which are critical for estimating price impacts but often subject to uncertainty and data gaps. Where liquidity
parameters are unavailable or markets are illiquid, second-round effects may be understated. Additionally, investor
behavior, liquidity buffer usage, and repo funding are simplified representations of complex real-world dynamics.
Therefore, MILD outputs should be viewed as scenario-based indicators of vulnerability and amplification, not as point
forecasts, and are best interpreted alongside expert judgment and complementary analyses. Overall, MILD is useful for
identifying fund vulnerabilities and market spillovers under alternative behavioral and market-impact assumptions. Its
outputs should be read as scenario-based indicators, given their sensitivity to data quality, redemption calibration,
liquidation behavior, and market-depth assumptions.
FSAP: Common Approach and Country-Specific
Adaptations
While FSAP applications share a common scenario-based, top-down methodology for tracing liquidity needs and
cross-sector spillovers, their scope and implementation are tailored to jurisdiction-specific financial structures,
vulnerabilities, and available data . The country analyses should therefore be read as combining a common analytical
framework with local data and institutional features, as well as staff assumptions and hypotheses where empirical
evidence is limited.
Early work
Several IMF country works tackled systemic liquidity risk assessment well before systemwide stress testing
tools were made available. The2017 Luxembourg  FSAP and Article IV consultation examined liquidity contagion effects
between banks and investment funds, focusing on the spillovers from investment funds that face substantial redemption
to banks when the stressed funds liquidate domestic bank deposits. The Article IV consultation with Andorra ,Mauritius ,
andSweden14discussed international reserve adequacy to withstand FX liquidity stress from the financial system using
bank liquidity stress testing results, including a stressed liquidity coverage ratio (LCR).
Some of these analyses led to operational policy recommendations . Andorra’s, Mauritius’, and Sweden’s examples
led to recommendations to build up more international reserves so that the central bank could play the of lender of last
14 Policy actions in Sweden in the past decade provide an interesting case of redesigning some aspects of LCR and international reserve
management to better support withstanding cross-border FX liquidity shocks. While Sweden is not a dollarized economy, banks rely
substantially on US dollar and euro cross-border wholesale funding. The Riksbank strengthened its international reserves with external
borrowing and bilateral central bank swaps during the GFC and the COVID-19 crisis. However, it started to build net reserves more recently
and set the currency structure of international reserves to match the FX liquidity needs. It also guided  banks to satisfy Swedish krona, euro,
and US dollar LCRs separately with diversification requirements of HQLA to avoid the concentration of liquid assets in Swedish-covered
bonds.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 16

INTERNATIONAL MONETARY FUND 19resort (LOLR) role. The 2018 Armenia  FSAP and IMF lending program recommended changing the design of reserve
requirements based on the systemwide FX liquidity concept without laying out quantitative details. Armenia has a floating
exchange rate regime and faces relatively high levels of dollarization. While banks’ main liquid asset buffers are central
bank reserves, they must satisfy their reserve requirements in local currency, even for the portion earmarked for FX
deposits, creating significant FX liquidity mismatches. The FSAP recommended changing this rule so that banks satisfy
their FX reserve requirements in FX. While currency composition of reserve requirement typically receives little attention
when examining the design of requirement as a monetary policy and liquidity management tool, it plays a critical role in
setting the structure of banks’ liquid asset buffer.15
Systemwide analyses
Example of key issues by the stages of financial system development
The Excel-based systemwide liquidity stress testing tool has been applied in several technical assistance
missions covering low-income economies, emerging markets and high-income commodity exporters, and has
been used to identify and illustrate the different systemwide risks each group of countries face:
Low-income country . In this example, the country has large twin deficits financed mostly by official-sector loans
and grants to the government, but foreign investors also directly invest in local currency government bond
markets. The financial system is dominated by commercial banks, small, and dollarized. Therefore, main
aggregate liquidity risks could arise from scenarios with public finance stress that leads to more extensive
external financing needs, FX deposit run by residents, and exit by foreign investors from the local-currency
government bond market, which led to FX market intervention to curb excessive volatility in the past. Results
show that the system (including the central bank) can withstand aggregate FX liquidity stress unless there is a
generalized panic run on domestic FX deposits or external financing needs for the government jumps.
Nonetheless, financial dollarization and thin FX liquid asset buffers of banks make the banking sector vulnerable.
Recommendations include strengthening banks’ FX liquid buffers by allowing banks to satisfy reserve
requirements earmarked to FX deposits in hard currency and to hold global safe assets if FX LCR is
introduced.16
Emerging market economy . The tool was applied to a few EMs with some or notable external vulnerability.
Their cases are represented by the illustrative example explored in Oura (2022)—a hypothetical Emerging
Market (EM) with substantial external borrowings—especially by sovereigns, NFCs, and banks to a lesser
extent—and partial dollarization. In the example, nonbank financial intermediation and capital markets are
underdeveloped, and banks and NFCs have a large footprint in the financial system. Changes in global financial
conditions and capital outflows are key aggregate liquidity risks. Capital outflow shocks could transmit noticeably
across domestic sectors because NFCs have substantial FX deposits at domestic banks, and banks’ FX HQLA
are largely FX reserve deposits at the central bank. NFCs are the most vulnerable sector, as they have more
significant FX liquidity mismatches than the other sectors. The extent of contagion effects from NFCs depends
15 In contrast, some countries consciously use currency requirements of reserve requirements to strengthen international reserves and for
liquidity management purposes. For example, the central bank of the Republic of Türkiye introduced a policy allowing banks to fill their
reserve requirement for domestic currency deposits in FX and gold, but not vice versa, in the early 2010s. Such policy boosts gross but not
net international reserves.
16 Banks are not allowed to invest in foreign assets for fear of investing in risky assets.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 17

INTERNATIONAL MONETARY FUND 20critically on their pecking order of asset liquidation, because NFCs have both foreign assets and domestic FX
deposits. The resilience of the banking sector depends more on NFCs’ behavior and the degree of panic run by
the household sector than the direct impact of capital outflows. Similarly, banks have global safe assets and FX
reserve deposits at the central bank. If they primarily use reserve deposits, it could reduce international reserves
substantially. The central bank may reduce the FX reserve requirement ratio to increase the usable FX liquid
asset buffers for banks before considering Emergency Liquidity Assistance (ELA). Also, it should monitor and
survey the composition of liquid assets buffers of banks and NFCs, motivation to hold those assets, and
contingent liquidation plan.
High-income commodity exporter . In this case, the country has a large current account surplus and net
positive international investment position. Most of the foreign assets are held by the sovereign wealth fund,
separated from the international reserves of the central bank. The financial system, dominated by banks, is
usually awash with liquidity from oil export receipts, and the central bank issues papers to absorb liquidity.
However, the system has been hit by a few stress episodes related to oil price swings, among others. The
central bank adopts a fixed exchange rate regime that requires a high share of central bank money to be backed
by international reserves, which means both local currency and FX liquidity stress impact the central bank
balance sheet and international reserves (El Hamiani Khatat and Veyrune 2019). Indeed, in some stress
episodes, the central bank had to ask to boost its capital and corresponding international reserves to the SWF.
The mission suggested that the central bank consider introducing more contingent, temporary flexibility with the
backing requirement of central bank money by international reserves. It also recommended using during distress
episodes the reserve requirement ratio, which had been held constant throughout the cycle, because the policy
tool’s main objective was to fill in the lack of deposit insurance rather than liquidity and monetary management
objectives. Moreover, given these constraints for the central bank to play the role of LOLR, introducing
preemptive prudential measures such as FX LCR is essential. Staff also recommended understanding better the
driver of a recent increase in banks’ foreign asset holdings, which could mitigate the contagion effects on the
central bank.
Application and enhancement of Excel-Based systemwide analysis tool
A more extended version of the tool was applied in recent FSAPs using additional granular and often
confidential data in several EMs and small open AEs . FSAPs usually have access to detailed supervisory reporting
data—especially detailed LCR data—for banks and certain types of NBFIs, which helps improve exercises’ accuracy.
Philippines
The 2021 Philippines FSAP  assessed the liquidity linkage between banks and NFCs due to temporary loan
moratoria introduced during the COVID-19 crisis . It supplemented BSA with supervisory data of banks and financial
statements of publicly traded NFCs to obtain more details about liquid asset buffers, funding instruments, and their
maturities. Loan moratoria stop debt service cash inflows from banks and outflows from NFCs for the firms that applied to
the program. The key assumptions representing the two sectors’ linkage are NFC loan refinancing rate—a banks’ choice
variable—and NFCs’ asset liquidation decisions. While LCR assumes low refinancing rates to preserve liquidity for banks,
this exercise also examined higher refinancing rates in addition to moratoria.
This case is an example where NFCs—outside of the perimeter of prudential regulation—could be systemically
important for financial stability. NFCs’ liquidity positions weaken as the scenario assumes drops in earnings because
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 18

INTERNATIONAL MONETARY FUND 21of the lockdown, but loan moratoria could relieve some pressures. Moratoria, at first, seems to shift liquidity away from
banks to NFCs. However, NFCs may need to tap into their liquid assets buffers if they do not use moratoria, earning
shocks (i.e., aggregate liquidity shock) are large, and banks reduce loan refinancing rates to conserve their liquidity. If
NFCs primarily liquidate domestic bank deposits, then liquidity stress will be transferred to banks even without moratoria.
Staff recommended that the central bank use its new macroprudential power given by amended central bank law, which
allows it to seek information from any entities in the country.
Chile .
The2021 Chile FSAP  work used institution-level data of banks, mutual funds, and pension funds and showed
institution-level vulnerabilities in addition to aggregate risks.  The Chilean financial system has sizeable pension and
mutual fund sectors that provides substantial wholesale bank funding and corporate credit. The system experienced a
systemic liquidity stress in 2019 as retail investors switched funds and reallocated their portfolio away from long-term
domestic fixed-income assets to foreign assets in an unprecedented manner due to advice from social-media-based
financial advisors. The portfolio reallocations and redemptions put significant pressure on bank and corporate bonds as
well as the Chilean peso, and the central bank responded by expanding the collateral framework for liquidity operations to
include unsecured bank bonds and intervened in the FX spot market to curb excess volatility. Bank funding risks were
heightened by the lack of a functioning secured interbank lending market to backstop wholesale funding.
Liquidity stress tests of banks, pension, and mutual funds highlighted continued vulnerability to similar events.
The FSAP recommended improving pension fund regulation and investment options to promote long-term investment and
minimize excessive switching, strengthening the mutual fund liquidity management framework, introducing bank liquidity
stress tests, facilitating the development of the interbank repo market, and strengthening central bank collateral and ELA
framework.
Tϋrkiye .
The2023 T ϋrkiye FSAP took place during episodes of macrofinancial volatility where the central bank took
unusual measures to secure international reserves (i.e., FX liquidity). The economy suffered from persistently high
inflation, that increased to almost 80 percent in mid-2022 and marked depreciation of the Turkish Lira. FX liquidity risks
had risen along with deposit dollarization and low international reserves of the central bank. A substantial nexus existed
between the central bank and commercial banks, whose FX assets held at the central bank were about double the readily
available FX gross international reserves and gold holdings of the central bank in mid-2022.17 Moreover, almost three-
quarters of central bank FX liabilities were owed to domestic banks in the form of deposits or swaps. This alone was
larger than total central bank FX reserves assets and was a large share of banks’ FX liquid assets.
Using the enhanced Excel-based tool, the FSAP closely examined vulnerability to a tail-risk scenario capturing
FX liquidity risks and accounting for the interdependence between the central bank and commercial banks.  Bank
liquidity stress test adjusted starting point HQLA and LCR, including only the central bank’s readily available FX liquidity—
excluding gold, non-hard currency FX, SDRs, among others. Systemic FX liquidity stress tests assessed the impact of
stress stemming from NFCs, households, and general government on banks and the transmission to central bank
international reserves, incorporating large off-balance FX swap positions of banks vis-à-vis other sectors. These tests
17 Readily available FX gross international reserves refer to the portion of the central bank’s foreign exchange reserve assets that can be
deployed immediately to meet banks FX liquidity needs, excluding less liquid or encumbered components such as gold, SDR holdings, non-
hard-currency assets, and reserves tied up through certain swap or deposit arrangements.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 19

INTERNATIONAL MONETARY FUND 22found banks can withstand moderate FX liquidity stress but highlighted the vulnerability to severe FX liquidity outflows,
which could potentially drain central bank international reserves to low levels.
Iceland .
The2023 Iceland FSAP  examined resilience against systemic liquidity events driven by both domestic and global
factors, including the capacity of the central bank to provide FX liquidity backstop.  As a small open economy with
a large financial sector with active cross-border transactions, Iceland is vulnerable to aggregate FX liquidity shocks if
foreign investors take out deposits or sell off Icelandic assets. Its financial system is dominated by a concentrated
banking system, and it also has a rich NBFI sector including pension funds and investment funds. Without a reserve
currency, the central bank’s ability to provide FX liquidity backstop is limited to international reserves.
FSAP applied the Excel-based framework to capital outflow scenarios.  The exercise included FX deposit
withdrawals by nonresident and resident nonfinancial sectors, asset reallocation of pension and investment funds, and
exits from international bonds issued by Icelandic entities. FX liquidity stress to domestic NBFIs and nonbank sectors
could easily spill over to banks if stressed segments liquidate their local bank deposits to fill their respective liquidity gaps.
The exercise indicated that single-factor stress on each liquidity risk factor included in the capital outflow scenario alone is
unlikely to exhaust banks’ FX liquidity buffer. Only a combination of severe stress on each factor could push banks into
FX liquidity shortage. Yet, the central bank had enough international reserves to fill in banks’ FX liquidity shortage, partly
because the central bank greatly boosted their gross international reserves with external borrowing. More than 40 percent
of the gross international reserves were funded by external borrowing.
India
The2024 India FSAP  analyzed links among banks, Non-Banking Financial Company (NBFCs), and bond funds.
NBFCs are finance companies reliant on wholesale funding and bank loans and usually provide loans focusing on certain
segments (e.g., infrastructure, microfinance, consumers, etc.) Past distress episodes stemmed from concentrated credit
risks in the infrastructure sector. In the mid-2010s, defaults by power companies triggered a banking crisis, heavily
impacting state-owned banks. Later, major NBFCs defaulted on short-term borrowings after credit stress from
infrastructure lending that reduced cash inflows, worsened by low liquid asset buffers under limited regulation. Bond
funds—key NBFC financiers—reallocated away from NBFC debt, further straining liquidity. During the pandemic, loan
moratoria, closure of major bond funds, and heavy redemptions from bond funds by institutional and corporate investors
intensified NBFC liquidity stress. In response to these events, the authorities implemented various reforms, including
liquidity regulations for bond funds and set up industry-pre-funded Corporate Debt Market Development Fund (CDMDF)
with government backstop that can provide liquidity to corporate bond market during distress episodes.
The sectoral and systemwide liquidity analysis confirmed persistent vulnerabilities . NBFCs’ concentrated
exposures to structurally vulnerable infrastructure sector—shifted from banks even more—low liquid asset buffers,
reliance on wholesale funding, periodic bond fund redemptions tied to tax and bill payment cycles, central bank collateral
policies limited to sovereign bonds, and banks’ reluctance to lend to stressed NBFCs even with central bank support.
CDMDF could facilitate funds’ liquidation of corporate bonds, but the firepower was not sufficient to respond to all sales
pressures. However, given India’s relatively closed capital account, liquidity stress mainly affects how liquidity is
distributed, rather than causing aggregate losses or FX shortages unlike other EMs.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 20

INTERNATIONAL MONETARY FUND 23Bespoke Analyses
Mexico
The2022 Mexico FSAP18 substantially enhanced the tool to gauge the impact of capital outflows from local
sovereign bond markets on the rest of the domestic financial system (Figure 3). Mexico’s financial system is well
integrated with global capital markets with significant foreign direct investments (FDIs) to NFCs and direct foreign
investment in domestic sovereign bond markets. Mexican financial assets, including the peso, are also traded as proxy
assets representing the EM asset class. Domestic banks and NBFIs (especially investment funds, pension funds, and
insurers) are exposed to common assets—especially sovereign debt securities, and counterparty risk via direct lending
and repo operations. NFCs are exposed to offshore refinancing risks, though they also have substantial foreign assets.
Against this backdrop, the FSAP examined a capital outflow scenario from local sovereign bonds and its impact
on bond valuation and liquidity needs across domestic sectors. Capital outflows reduce bond valuation and cause
liquidity needs to fill in margin calls from repo and derivatives positions.19 The FSAP used highly granular BSA data,
including institution-level data for commercial and development banks and some NBFIs, their detailed exposure to local
sovereign bonds (cash, repo, and derivatives), contingent claims such as credit lines, and detailed liquid asset buffer
information (including unencumbered securities that are not pledged as collaterals for secured funding and some
derivative transactions).
They also examined the sensitivities of the results to specific assumptions. Assumptions are generated as sets of
correlated shocks to key asset prices and available funding under the same qualitative capital outflow scenario—as well
as to the second-round effects from further asset price declines due to fire sales. Stressed institutions are assumed first
to liquidate cash, then phase out short-term funding, and finally pledge unencumbered securities for secured borrowing.
The exercise also examined an alternative pecking order of liquidation within each step (e.g., which assets to pledge
first). Overall, various sensitivity and liquidity policy experiments show commercial banks’ central role in ensuring the
liquidity of the financial system by backstopping the liquidity needs of all other agents while signaling potential
vulnerabilities in development banks when facing market behavioral constraints under stress.
18 See also the working paper detailing the methodology by Ding, Laliotis, and Toffano (2024).
19 The exercise reflects the regulatory framework and market practices prevailing in 2022. Mexico’s margin requirements for non-centrally
cleared OTC derivatives entered into force in 2025 and could affect margin-call and liquidity dynamics in future stress scenarios.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 21

INTERNATIONAL MONETARY FUND 24Figure 5. Mexico: Design of Systemwide Liquidity Analysis
Source: IMF, 2022b Mexico FSAP, technical note on systemic risk analysis and stress testing.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 22

INTERNATIONAL MONETARY FUND 25By comparison, a comprehensive systemic liquidity analysis has been more challenging to conduct in AEs
because of the complexity of their system.  AE systems tend to have a much richer nonbank financial intermediation
sector and complex financial instruments. As a result, the BSA matrix could be partial—missing critical linkages among
NBFIs as in the US—or insufficient—missing much off-balance sheet information (such as derivatives and associated
margin calls, repos, credit lines, structured funding, securitized assets, and leveraged exposures). At the same time,
large, highly granular data are available for specific segments in some countries—such as individual security-level holding
data for investment funds, banks, and in some cases, insurers, which are helpful to measure contagion effects through
common exposures. FMI-collected activity-based data could offer unique perspectives, but they have never been used in
FSAPs due to their confidentiality and complexity. Still, there have been recent efforts to enrich systemic liquidity
analyses in AE FSAPs.
France, Ireland, and Sweden
The2019 France FSAP  provided extensive network analysis focusing on risks from common exposures among
banks, mutual funds, and insurers.  The French financial system mainly consists of banks, insurers, and investment
funds, many of which are connected under a financial conglomerate structure. Most conglomerates are internationally
active, with diversified assets and liabilities across sectors and borders. Against this backdrop, the French authorities
initiated long-term data gap initiatives to better understand the interconnectedness across sectors and within financial
groups. At the time of the FSAP, the authorities had constructed the data set showing security-level exposures in
marketable securities (covering both domestic and foreign securities) for banks, insurers, and funds. The FSAP team
used this unique data and applied network analyses to identify key characteristics of the interconnectedness, focusing on
direct exposures and common exposures measuring similarities of balance sheet counterparts.
The exercise found that all three sectors increased exposure to NFCs and French sovereign bonds in the 2010s.
Banks and insurers reduced common exposures since the 2012 FSAP. At the same time, funds diversified their
counterparties by increasing their cross-border exposures but following the same pattern, increasing common exposures
and, therefore, vulnerability to systemic risk. Also, funds’ domestic exposures are concentrated in funding from insurers
and investment in bank bonds, escalating interconnectedness in the system. The 2022 Sweden  and 2022 Ireland  FSAPs
included similar interconnectedness analyses, including the Sweden FSAP’s work to gauge the price impact of
investment funds’ fire sales. While these exercises were not systemic liquidity stress tests, they provided useful
background information to design future stress testing exercises and priorities for additional data building.
United States
The US financial system has a rich NBFI sector and complex financial instruments, including large mutual fund
and money market fund sectors that are prone to redemption and market risks.  Also, capital markets are deep and
broad—even credit risks are actively traded as securitized loans and credit derivatives by a range of banks and NBFIs,
escalating the importance of contagion through common exposures. Over half of the financial intermediation takes place
outside of the banking system, and the role of nonbank financial intermediation has grown visibly since the GFC. NFCs
actively finance in markets, and risks from NFC debt (e.g., leveraged loans, high-yield and private debt markets, and
related products such as collateralized loan obligations (CLOs)) were one of the main risks highlighted in the 2020 U.S.
FSAP .
The FSAP conducted numerous sectoral stress tests, including banks, insurers, mutual funds, money market
funds, and NFCs, and connected them to gauge contagion effects (Figure 4).  Building on these sectoral results, the
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 23

INTERNATIONAL MONETARY FUND 26FSAP also assessed the transmission of the risks from NFC debt across the financial system, focusing on an instant
market shock lasting a month and leading to immediate asset liquidation. A BSA-like analysis showed that direct
exposures to the US corporate sector are concentrated among NBFIs, while banks’ exposures are mostly term loans and
credit lines. Accordingly, NBFIs would suffer larger direct losses from corporate debt market distress events than banks.
Stress on NBFIs, especially mutual funds, spills over to other segments through direct linkages (such as liquidity stress to
banks that provide credit lines to stressed mutual funds) and indirect linkages (such as second-round effects on corporate
debt spreads due to mutual funds’ asset liquidation, which intensifies initial marked-to-market losses from corporate
securities to other corporate debt investors).
The analyses showed that asset liquidation by mutual funds could lead to significant price impacts, especially
on EM and high-yield bonds.  While their impact on systemically important banks’ capital is limited, the marked-to-
market losses could have a non-negligible impact on some NBFIs. At the same time, the FSAP emphasized the potential
sensitivity of the results to alternative market behaviors (such as the order of asset liquidation), model and estimation
uncertainty about fire sales-price impact relationships, and systematic mispricing of risks—all of them could both over-
and underestimate the total impact.
Figure 6. United States: Schematic of the Systemic Liquidity Risk Transmission Mechanisms
Source: 2020 US FSAP, technical note on risk analysis and stress testing in the financial sector.
Euro Area
This exercise advances systemwide risk analysis by incorporating a wider range of financial institutions, margin
calls from derivatives, and collateral calls from repos (Figure 5).  It includes investment funds (such as hedge funds,
LDI funds, and Undertakings for Collective Investment in Transferable Securities (UCITS)), insurers, banks, and MMFs. It
goes beyond standard fund stress tests by jointly modeling margin calls, repo haircuts, redemptions, and asset sales, and
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 24

INTERNATIONAL MONETARY FUND 27by quantifying second -round price impacts that feed back into OFIs. Notably, it distinguishes between immediate (two-
day) and short-term (two-week) dynamics to capture constraints arising from T+2 settlement where margin and collateral
calls have to be met instantly, while the proceeds of asset sales and redemptions materialize only after two days. This
approach, which uses transaction-level supervisory data for securities, repos, and derivatives to trace
interconnectedness, sets it apart from prior analyses that exclude off-balance sheet transactions, making the results more
relevant for macroprudential surveillance and policy design.
The analysis shows how liquidity stress originating in investment funds can propagate across the financial
system through multiple, reinforcing channels. Initial shocks—driven by market price declines, margin calls, and
investor redemptions—force funds to draw on cash buffers (bank deposits and MMF shares), liquidate or repo assets,
and adjust derivatives positions. These actions transmit stress to core funding and securities markets, particularly
sovereign, bank, and corporate bond markets, where concentrated sales depress prices and reduce market liquidity.
Because euro -area funds hold globally diversified portfolios, spillovers are not confined domestically but can quickly
extend cross -border, amplifying volatility in global fixed -income markets.
Central spillover channels differ across sectors.  Banks are affected through several channels: potential missed
derivative margin calls from stressed funds increase counterparty credit risk; repo market strains reduce funding
availability; and deposit withdrawals due to fund redemptions weaken bank liquidity positions. MMFs play a pivotal
amplifying role, as they provide repo liquidity (reverse repo) to funds but may themselves face large redemptions, since
many institutions hold MMF shares as cash equivalents, leading to sales of commercial paper and short -term bank debt
assets that tighten wholesale funding conditions—echoing dynamics observed in March 2020. Insurers contribute to
spillovers mainly through liquidity needs from margin calls on derivatives and valuation losses on asset holdings, which
can reinforce procyclical asset sales and increase funding pressures elsewhere in the system.
Second -round effects materially magnify initial shocks (Figure 5).  Asset sales by funds and spillover sales by MMFs
and insurers generate endogenous price impacts, raising yields and spreads and increasing further margin and
redemption pressures in a feedback loop. While aggregate solvency impacts on banks and insurers remain contained as
market stress is presumed temporary, the analysis highlights that liquidity shocks can propagate rapidly and non- linearly
through interconnected balance sheets and markets, even in the absence of large defaults. The findings underscore that
NBFI liquidity distress is a systemic, not sectoral, phenomenon, reinforcing the need for systemwide monitoring,
coordinated stress testing across sectors, and policies aimed at reducing procyclicality and excessive reliance on market
liquidity under stress.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 25

INTERNATIONAL MONETARY FUND 28Figure 7. Euro Area: Schematic of the Systemic Liquidity Risk Transmission Mechanisms
Source: 2025 Euro Area FSAP, technical note on risk analysis and stress testing in the financial sector .
Note: The range of market and price impacts reflects alternative behavioral assumptions for stressed sectors.Market Shock
 Term structure
 Credit spread
 Equity
Asset revaluation
 Securities
 Derivatives
 In-sample funds sharesAggregated
liquidity demand
 Redemption (flow-
performance)
 Margin calls on
derivatives
 Collateral calls on repo
Mitigating actions
 Deposit withdrawal
 Suspend reverse repo
roll-over
 New repo
 Asset sales
 Fund shares
redemptionsSpillovers
 Core markets
 Funds
 Banks
 Insurances
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 26

INTERNATIONAL MONETARY FUND 29Key Takeaways
FSAP experience underscores the need to tailor systemwide liquidity analysis to each jurisdiction’s financial
structure, vulnerabilities, and data availability. The applications above show that key risk drivers, institutions, markets,
regulations, trading practices, and behaviors vary widely across countries and over time. In less complex and more
externally exposed economies, the Excel-based approach has helped trace how capital outflows, FX liquidity pressures,
and nonfinancial-sector behavior transmit stress through domestic financial linkages and affect central banks’ capacity to
provide backstops. The central participants also differed markedly—ranging from pension funds in Chile and NBFCs in
India to foreign investors in Mexico’s local-currency sovereign bond market, central bank reserves in Türkiye, and
nonfinancial corporates in the Philippines. In more advanced, market-based systems, applications have increasingly
focused on bank–NBFI interlinkages, common exposures, fire-sale dynamics, derivatives and repo-related margin and
collateral calls, and stress transmission through core funding and securities markets. Given system complexity and
persistent data gaps, truly comprehensive systemwide analysis remains challenging for both the IMF and national
authorities; most exercises therefore focus on specific instruments or sectors.
These exercises were presented as exploratory, reflecting wide uncertainty around system resilience and its
measurement, as in similar work by national authorities.  Results were highly sensitive to assumptions about market
participants’ behavior, the specification and calibration of fire-sale price dynamics—particularly difficult to estimate in
crisis conditions—the perimeter of institutions and instruments covered, and the scenarios considered (see the Way
Forward section). Accordingly, most exercises avoided firm resilience assessments and instead focused on identifying
key transmission channels, systemic actors, data gaps, safety-net arrangements, and priorities for future analysis. Unlike
sector-specific bank solvency or liquidity stress tests, systemwide analyses lack agreed hurdle rates—that is, quantitative
indicators and thresholds for determining whether institutions or the system “fail” the test—including for institutions such
as hedge funds. Moreover, systemic liquidity stress can arise even when institutions meet regulatory requirements. For
example, a bank may satisfy the Liquidity Coverage Ratio, calibrated over one month, and the Net Stable Funding Ratio,
calibrated over one year, yet still lack sufficient same-day cash to meet derivatives margin calls. While prior vulnerability
analysis helps identify the risks and channels to examine, the stress test adds value by quantifying their potential scale
and propagation under alternative, internally consistent scenarios. These scenarios may be historically grounded or
deliberately more severe and exploratory, so their results are conditional rather than probabilistic assessments.
As a result, recommendations have generally been “soft,” focusing on methodological advances, stronger
supervision, and closing data gaps . Unlike bank stress tests, requiring participants to raise capital or liquidity buffers in
response to systemwide vulnerabilities may not necessarily strengthen overall resilience. If vulnerabilities are
concentrated in certain investment funds, for example, requiring them to hold larger liquid assets could create new
spillover channels, depending on the assets held. Greater holdings of bank deposits could strengthen fund-bank linkages,
while larger holdings of sovereign securities could amplify second-round fire-sale effects in sovereign bond markets.
Similarly, requiring funds to establish contractual credit lines with banks could transfer liquidity risk to the banking system.
The international financial stability community, including leading central banks and regulators, has not yet reached an
agreed solution for managing systemwide liquidity risks, including the appropriate role of central bank backstops.
Way Forward
Systemwide liquidity stress testing tools that capture interconnectedness across sectors and institutions remain
experimental, partly due to data gaps.  Effective risk analysis depends on cross-sectoral interconnectedness data
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 27

INTERNATIONAL MONETARY FUND 30among banks, NBFIs, and, when relevant, non-financial or public sectors. Data on NBFIs, particularly lightly regulated
entities, is incomplete (see Table 1). Efforts like the G20 data gap initiatives20 have prompted countries to collect sector-
aggregate flow-of-funds by counterpart, such as IMF’s BSA data (IMF 2015). FSB’s more segmented data are available
for many jurisdictions, but these provide only high-level mapping and lack depth for systemwide analysis. They also often
miss key some cross-border transactions—important for hedge funds incorporated in tax havens—and off-balance sheet
items like derivatives, repos, credit lines, and other contingent assets or liabilities. National supervisors may gather
activity-based information from transaction-level data held by FMIs, but processing these is resource-intensive and
technically complex, as shown in the Euro Area FSAP.21 Additionally, integrating sectoral data is difficult in many places
due to its highly confidential nature, hindering cross-agency collaboration.
In the near term, the IMF and some national authorities are leveraging available but often underused data, along
with bottom-up exercises, to address information gaps.  Two main top-down approaches are used to shed light on the
dark corner of finance, such as hedge funds and private finance. The first utilizes confidential counterparty data from
regulated entities, especially banks, which can help map significant NBFI activities, identify banks’ concentrated or
common exposures to them, and assess spillover risks to banks, for example by using regulatory data on large exposures
as in Valderrama and Varghese (2026). The second approach relies on transaction-level data collected by FMIs to
monitor margin and collateral calls under stress scenarios and pinpoints which agents might face substantial credit or
liquidity losses. While full resilience analysis requires institutional-level data on liquidity and capital buffers and available
credit/repo lines—currently feasible only for regulated entities—mapping risk concentrations remains a valuable tool for
identifying markets and institutions that could trigger systemwide stress. This approach will require significant
collaboration with national authorities beyond FSAP, as it relies on highly confidential data that the IMF cannot directly
access and involves labor-intensive big data management.
Another challenge in establishing robust systemwide liquidity stress testing is the significant influence of
behavioral factors, which are difficult to pin down . Decisions are the results of a complex and continuous optimization
process across a wide range of markets and products that are difficult to model in a reduced and realistic way. In addition,
during periods of stress psychology-driven behavior can materially affect market outcomes, as demonstrated in
behavioral finance and economics literature (see Hirshleifer 2015, building on foundational work by Kahneman and
Tversky, 1979), and can give rise to outcomes that are difficult to predict. As illustrated in the examples detailed in
previous sections, the way each agent responds to liquidity stress is crucial in determining the extent of liquidity contagion
effects. While theoretical frameworks offer guidance, actual behavior could be different and hard to estimate, especially
since it varies across agents, over time, and across jurisdictions. Consequently, FSAP exercises typically examine a
range of behavioral assumptions to identify key parameters that significantly affect results and also rely on expert
judgment from market surveillance and discussions with national supervisors. Increasingly, bottom-up exercises are
helping to address this gap; for instance, the 2025 Euro Area FSAP partially relied on behavioral patterns observed in the
20 The initiative began in 2009, completed its second phase in 2022, and is expected to begin its third phase, with continued annual monitoring.
The last progress report (IMF-FSB, 2022) stated that challenges remained in securities financing transaction data, securities statistics,
sectoral accounts, and cross-border exposures of nonbank corporations, among others (see website:
https://www.imf.org/en/News/Seminars/Conferences/g20-data-gaps-initiative).
21 Other examples of such analyses include Fache, Jukonis, Letizia, and Gravanis (2020), who examine European derivatives transaction data;
Hüser, Lepore, and Veraart (2024), who analyze the Gilt repo market; and Jukonis, Letizia, and Rousova (2022), who examine the impact of
derivatives collateralization on investment funds’ liquidity risk. Paddrik, Rajan, and Young (2020) and Levels, et al. (2018) examine
contagion in the credit default swap (CDS) market using activity-based data from clearinghouses. Huang, Menkyeld, and Yu (2021) modeled
interconnectedness through CCP.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 28

INTERNATIONAL MONETARY FUND 31BoE’s SWES. Lessons from these bottom-up exercises can then inform advanced behavioral modeling, like agent-based
models (ABMs), helping to build more empirically grounded stress-testing models.22
Behavioral assumptions should also reflect market microstructures, transaction types, and clearing
arrangements from a systemwide perspective.  As seen in the Euro Area case, factors such as margin and collateral
calls, settlement cycles (T+2), and the role of FMIs—whether trades are cleared by CCPs or remain bilateral—can
materially affect the outcome. These practices differ widely across jurisdictions, institutions, and instruments, and are
often opaque, with even CCP margin formulas lacking full transparency (BCBS, CPMI and IOSCO, 2022, FSB 2024). As
money markets shift from interbank to instruments like repos and derivatives involving more participants, including NBFIs,
understanding these details becomes more important. Furthermore, CCP rules and stress tests typically focus on CCP
stability, which may not align with systemwide risk objectives. In systemic shocks, stress can originate from CCP
members or large clients—as seen in the Archegos case—even when CCPs remain resilient. Therefore, CCP stress
testing—on its own or as a part of systemwide analysis—should evolve to incorporate systemwide perspectives, as
demonstrated in the BoE’s recent SWES (BoE, 2024).
Moreover, agents’ actions must be consistent in a systemwide analysis, which requires deviating from standard
sectoral stress testing assumptions.  Systemwide risk analysis requires combining sectoral analysis with adjusted
parameters to ensure behavioral consistency across agents. For instance, it is unrealistic to assume that household
investors simultaneously redeem from all investment funds and withdraw from all banks, as their funds must remain within
the system (unless moved to options like gold, crypto assets, or foreign assets that are “outside” of domestic financial
systems). In standard liquidity stress tests, banks exiting the stress with ample liquid asset buffers are generally
interpreted as a positive outcome. In a system -wide setting, however, such outcomes may amplify contagion and
generate spillovers if they arise from precautionary liquidity hoarding that constrains funding to other institutions or
sectors. In investment fund liquidity stress tests, even if funds remain resilient due to their liquid asset buffers, drawing
down deposits from banks simply shifts the liquidity stress from funds to banks. A further distinction relative to standard
sectoral stress tests is that these exercises generally assume broadly adverse impacts across all participating institutions,
albeit to differing extents. In contrast, system -wide exercises allow for heterogeneous outcomes, whereby some
institutions or entire sectors may benefit under specific scenarios.
In this context, when comparing systemwide exercises, it’s crucial to clarify what defines the “system.”23 In IMF
analyses using the Excel-based tool, the system usually includes the entire economy—including nonfinancial and public
sectors. In tailored exercises, like the Euro Area FSAP and national authorities’ bottom-up approaches, the system often
refers to private financial institutions. Each approach has merits: broader sector coverage suits high-level, aggregate
analyses, while simplified sectoral and institutional coverage is necessary for modeling complex instruments like
derivatives and repos. For global liquidity analysis, including all major jurisdictions may be required. Ultimately, the
system’s scope should match the main questions, data availability, and practical constraints.
22 An ABM is a simulation-based approach that allows economic and financial system dynamics from the bottom up based on individual agents,
including firms, households, banks, NBFIs, and sovereigns, as needed. Some agents follow optimized rules while others could follow more
heuristic behavioral rules because of bounded rationality and other factors emphasized in behavioral finance literature.
23 The inside-outside (or public and private) theory of money (Gurley and Shaw, 1960; Lagos, 2006) helps clarify liquidity consistency. Inside
money typically means private money like bank deposits, repos, and MMF shares, while outside money represents sovereign liabilities, such
as currency and treasury bills. The distinction depends on how the “system” is defined—such as domestic or global. For example, global
liquidity arises from the interaction between private money and public money (global safe assets, central bank swap lines), as described by
Goldberg (2024). Brunnermeier and Niepelt (2019) incorporated these cross-border concepts and links to financial stability risks from runs
into their model.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 29

INTERNATIONAL MONETARY FUND 32Technical challenges also arise in estimating sale-price dynamics in highly illiquid markets with sparse trading.
These estimates are crucial for assessing second-round effects from asset liquidation at potentially fire-sale prices.
However, standard methods usually rely on asset price volatility, which may be nearly zero in markets with infrequent
trades. For example, the 2024 India FSAP investment fund analysis excluded spillover effects from sale-price dynamics
due to limited corporate bond trading, because they led to counterintuitive findings, where price impacts were greater in
actively traded sovereign bond markets than in smaller, illiquid corporate bond markets. In cases where standard price-
impact methods are not suitable due to illiquid markets, an equilibrium approach that infer prices by matching supply and
demand, may provide more reliable results, as explored by some authorities.
Conclusion
The IMF has made significant progress in developing top-down systemwide risk analysis—an important frontier
for financial stability—over the past decade. This approach is crucial for assessing systemic risks from NBFIs and
their spillover effects to banks, other NBFIs, and across borders given their systemwide interconnectedness.
Methodological advances have been published and applied in FSAPs. Early applications for less complex EMDEs helped
to identify areas for improvement and demonstrated how stress test results can inform policy recommendations on
systemic liquidity. Recent work has focused more on NBFIs, market finance, and new liquidity risks from margin and
collateral calls for more complex systems, aligning with FSB’s current initiatives (FSB, 2024b). Enhanced access to
transaction-level data, enabled by post-GFC reforms of financial market infrastructures like CCPs and data repositories,
has supported this progress.
Further progress is needed to strengthen analytical capabilities for assessing near-term financial stability risks
related to NBFIs and their interconnectedness.  For instance, a deeper understanding of the risks associated with the
increasing prevalence of hedge fund basis trades—financed through repo transactions amid rising public debt in core
markets—is essential in some core markets (see BIS Quarterly Bulletin, December 2025, and the October 2024 GFSR).
Such evaluations will increasingly depend on transaction-level data collected by FMIs, supplemented where possible by
partial entity or counterparty data reported by regulated institutions. Bottom-up exercises are another valuable approach.
All these methods demand significant resources and underscore the importance of close, ongoing collaboration with
national authorities, potentially requiring a multi-year engagement that extends beyond the FSAP timeline.
Yet, developing systemwide analysis tools is still a useful and informative endeavor.  Given the challenges,
systemwide risk analysis is usually not suited to draw strong conclusions about the resilience of the system upon shocks.
Nevertheless, these exercises are useful in identifying potential weak links, critical data gaps, priorities for strengthening
or streamlining supervisory and reporting frameworks, areas for improving data sharing and cross -agency coordination,
and regulatory features that could be adjusted to better support system -wide stability. It can also help identify industry
rules and practices that could help one sector’s resilience but possibly at the cost of the system, such as margin
practices.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 30

INTERNATIONAL MONETARY FUND 33Annex I. Coverage of NBFI and FMIs in recent FSAPs
Table I.1: Coverage of NBFI and FMIs in recent FSAPs—Stress Tests, Regulation and Supervision (2020–2025)
FSAPSolvency Stress
TestLiquidity Stress
TestSystemwide
AnalysisSupervision and Regulation
2025 Azerbaijan X
2025 Canada IC, PF IC, PF X IC, PF, IF
2025 China X IC, Markets, IF, FMI, NBFC
2025 Euro Area CCP IF X IC, IF, Markets, FMI
2025 France IF IC, Markets
2025 India NBFC NBFC, IF X NBFC, IC, Markets, IF
2025 Switzerland IC FMI, IC, Markets
2024 Japan IC IC, IF X IC, IF, CCP
2024 Luxembourg IC IC, IF X IF, IC
2024 Netherlands IC, PF IC, PF X IC, PF, Markets
2024 Spain FMI
2023 Belgium IC IC, IF X IC, FMI
2023 Botswana IC, PF X
2023 Iceland PF PF X PF
2023 Jordan X FMI
2023 Sweden IF X FMI
2023 Türkiye X IC, PF
2022 Germany FMI, IC
2022 Ireland IC IC, IF X IC, IF
2022 Mexico X
2022 South Africa X IF, IC, PF
2022 U.K. IC IC, IF CCP, IC, IF
2021 Chile IF, PF X IF, PF, IC
2021 Philippines X
2021 China—Hong Kong SAR IF CCP, FMI, IC, Markets
2020 Korea IC IC, Markets
2020 U.S. IC IF, IC X FMI, IC, IF, Markets
Note: IC = Insurance Companies, PF = Pension Funds, IF = investment Funds, NBFC = Non-Bank Financial Corporates, CCP =
Central Counterparties, Markets = Securities Markets, FMI = Financial Markets Infrastructure (includes CCPs, Central Securities
Deposito ries, payment systems). Including assessments undertaken by the World Bank for joint FSAPs.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 31

INTERNATIONAL MONETARY FUND 34References
Acharya, V. V., Pedersen, L. H., Philippon, T., and Richardson, M. 2017. “Measuring systemic risk”. Review of Financial
Studies , 30(1), 2–47.
Adrian, T. and Brunnermeier, M. K. 2016. “CoVaR”. American Economic Review , 106(7), 1705–1741.
Adrian, T., and H.S. Shin. 2010. “Liquidity and Leverage.” Journal of Financial Intermediation , 19(3), 418-37.
Agrawal, S., Broszeit, T., Singh, R., Sugimoto, N. Surti, J. and Vogelsang, S. 2025. “Pension Funds and Financial
Stability.” Global Financial Stability Note 2025/001, International Monetary Fund, Washington, DC.
Aikman, D., Beale, D., Brinley-Codd, A., Covi, G., H ϋser, A., and Lepore, C., 2022, “A Survey of Macroprudential Stress
Testing”, Bank of England Staff Working Paper No. 1033
Alfaro, L., Bahaj, S., Czech, R. Hazell, J. and Neam țu, I., 2024, “LASH risk and interest rates”, Bank of England Staff
Working Paper No. 1073.
Allen, F., E. Carletti, and D. Gale. 2009. “Interbank Market Liquidity and Central Bank Intervention.” Journal of Monetary
Economics , 56(5), 639-52.
Allen, F., and D. Gale. 1998. “Optimal Financial Crises”. The Journal of Finance, 53(4), 1245-84.
_______. 2000. “Financial Contagion.” Journal of Political Economy, 108(1), 1-33.
_______. 2004. “Financial Fragility, Liquidity, and Asset Prices.” Journal of the European Economic Association, 2(6),
1015-48.
Anand, K., Gai, P. and Marsili, M., 2012. Rollover risk, network structure and systemic financial crises. Journal of
Economic Dynamics and Control ,36(8), pp.1088-1100.
Aramonte,  S., Schrimpf,  A., and  Shin,  H. S. 2023. “Margins, Debt Capacity, and Systemic Risk”. BIS Working Papers
No. 1121. Basel: Bank for International Settlements.
Bakoush, M., Gerding, E. H., and Wolfe, S. 2019. “Margin Requirements and Systemic Liquidity Risk”. Journal of
International Financial Markets, Institutions and Money, 58, 78–95
Bank of England. 2023. “2023 CCP Supervisory Stress Test: results report”
_______. 2024. “The Bank of England's system-wide exploratory scenario exercise final report”
Baranova, Y., Coen J. Noss J. and Lowe P. 2017 , “Simulating Stress Across the Financial System: The Resilience of
Corporate Bond Markets and the Role of Investment Funds”. Bank of England Financial Stability Paper No. 42,
Bargigli, L., Di Iasio, G., Infante, L., Lillo, F. and Pierobon, F., 2015. The multiplex structure of interbank
networks. Quantitative Finance ,15(4), pp.673-691.
Basel Committee on Banking Supervision (BCBS) and International Organization of Securities Commissions (IOSCO).
2018. “Framework for Supervisory Stress Testing of Central Counterparties (CCPs)”.
Basel Committee on Banking Supervision (BCBS), Bank for International Settlements' Committee on Payments and
Market Infrastructures (CPMI), and International Organization of Securities Commissions (IOSCO). 2022. “Review of
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 32

INTERNATIONAL MONETARY FUND 35Margining Practices”. Basel: Bank for International Settlements. Conducted as part of the Financial Stability Board’s
work programme on non-bank financial intermediation
Bidder, R., Coen, J., Lepore, C. Silvestri L. 2024, “Whose asset sales matter?”. Bank of England Staff Working Paper No.
1088
Bouveret, A., 2017. “Liquidity Stress Tests for Investment Funds: A Practical Guide.” IMF Working Paper WP/17/226.
International Monetary Fund, Washington, D.C.
Bouveret, A. and Haferkorn, M., 2023. "Leverage and derivatives: The case of Archegos," Journal of Securities
Operations & Custody, Henry Stewart Publications, vol. 15(3), pages 238-250, June.
Brandão -Marques, L., Gelos, G., Ichiue, H., and Oura, H. 2022. “Changes in the Global Investor Base and the Stability of
Portfolio Flows to Emerging Markets.” Journal of Banking & Finance, 144, 106615.
Breeden, S., 2025, “A system-wide approach to system-wide resilience: CCPs and their users”. speech by Sarah
Breeden Given at ISDA Annual General Meeting, Amsterdam, Bank of England
Brunnermeier, M. K., and Niepelt, D. 2019. “On the Equivalence of Private and Public Money”. Journal of Monetary
Economics, 106, 27–41.
Brunnermeier, M.K., and L.H. Pedersen. 2008. “Market Liquidity and Funding Liquidity.” The Review of Financial Studies ,
22(6),2201-38.
Cetorelli, N., Landoni, M. and Lu, L., 2023. “Non-Bank Financial Institutions and Banks’ Fire-Sale Vulnerabilities”. FRB of
New York Staff Report , (1057).
Chen, R. and Kemp, E., 2023, “Putting Out the NBFire: Lessons from the UK’s Liability-Driven Investment (LDI) Crisis,”
IMF Working Papers 2023/210 (Washington: International Monetary Fund).
Coen, J., Lepore, C. and Schaanning, E., 2019. “Taking regulation seriously: fire sales under solvency and liquidity
constraints” Bank of England Staff Working Paper No. 793
Cont, R., Kotlicki, A. and Valderrama, L., 2020. Liquidity at risk: Joint stress testing of solvency and liquidity. Journal of
Banking & Finance ,118, p.105871.
Cont, R., and E. Schaanning. 2017. “Fire Sales, Indirect Contagion and Systemic Stress Testing.” Working Paper 2017/2,
Norges Bank.
Covi, G., Gorpe, M.Z. and Kok, C., 2021. “CoMap: mapping contagion in the euro area banking sector”. Journal of
Financial Stability ,53, p.100814.
Cunliffe, J., 2022, “Letter to Mel Stride, 5 October 2022”, Bank of England
Czech, R., Huang, S., Lou, D., and Wang, T. 2021. “An unintended consequence of holding dollar assets”, Bank of
England Staff Working Paper No.  953.
Diamond, D.W., and Dybvig P.H. 1983. “Bank Runs, Deposit Insurance, and Liquidity.” Journal of Political Economy,
91(3), 401-19.
Diamond, D.W. and Rajan, R.G., 2011. “Fear of fire sales, illiquidity seeking, and credit freezes”. The Quarterly Journal of
Economics ,126(2), pp.557-591.
Ding, X., Laliotis, D. and Toffano, P. 2024. “A Framework for Systemwide Liquidity Analysis”, IMF Working Paper
WP/24/104. International Monetary Fund, Washington, D.C.
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 33

INTERNATIONAL MONETARY FUND 36Duarte, F. and Eisenbach, T.M., 2021. Fire- sale spillovers and systemic risk. The Journal of Finance ,76(3), pp.1251-
1294.
Duffie D., Scheicher M. and Vuillemey G. 2015. “Central clearing and collateral demand”. Journal of Financial Economics,
Volume 116, Issue 2, 2015, Pages 237-256,
Eisenberg, L. and Noe, T.H., 2001. Systemic risk in financial systems. Management Science ,47(2), pp.236-249.
El Hamiani Khatat, M., and R. Veyrune. 2019. “Liquidity Management under Fixed Exchange Rate with Open Capital
Account. IMF Working Paper No. 19/58. International Monetary Fund, Washington, D.C.
Espinoza-Vega, M., and J. Sole. 2010. “Cross-Border Financial Surveillance: A Network Perspective.” IMF Working Paper
WP/10/105. International Monetary Fund, Washington, D.C.
European Systemic Risk Board (ESRB), 2024, “ESRB Annual Report 2024”, Frankfurt am Main: European Systemic Risk
Board
European Securities Market Authorities, 2023, “Final Report: Framework for the 5th ESMA Stress Test Exercise for
Central Counterparties”, ESMA 91-372-2557
European Central Bank (ECB). 2018. “Systemic Liquidity Concept, Measurement and Macroprudential Instruments.”
Occasional Paper Series No. 214. ECB Task Force on Systemic Liquidity.
Fache Rousová, L., A. Jukonis, E. Letizia, and M. Gravanis. 2020. “Derivatives-Related Liquidity Risk Facing Investment
Funds.” Financial Stability Review , 1. European Central Bank, Frankfurt.
Freixas, X., Parigi, B.M. and Rochet, J.C., 2000. Systemic risk, interbank relations, and liquidity provision by the central
bank. Journal of money, credit and banking , pp.611-638.
Financial Stability Board (FSB). 2020. “Holistic Review of the March Market Turmoil”, November 2020
______. 2024a. “Liquidity Preparedness for Margin and Collateral Calls: Final Report”. Basel: Financial Stability Board,
December 10.
______. 2024b. “FSB Work Programme for 2024”. Basel: Financial Stability Board. January.
______. 2025. “Global Monitoring Report on Nonbank Financial Intermediation”, December 2025
Fricke, D. and Wilke, H., 2023. “Connected funds”. The Review of Financial Studies ,36(11), pp.4546-4587.
Gai, P., Haldane, A. and Kapadia, S., 2011. Complexity, concentration and contagion. Journal of Monetary
Economics ,58(5), pp.453-470.
Goldberg, L. S. 2024. “Taking Stock: Dollar Assets, Gold, and Official Foreign Exchange Reserves”. Liberty Street
Economics, Federal Reserve Bank of New York
Gorton, G., and A. Metrick. 2012. “Securitized Banking and the Run on Repo.” Journal of Financial Economics , 104(3),
425-51.
Gourdel, R. and Sydow, M., 2023. “Non-banks contagion and the uneven mitigation of climate risk”. International Review
of Financial Analysis ,89, p.102739.
Greenwood, R., Landier, A. and Thesmar, D., 2015. “Vulnerable banks”. Journal of Financial Economics ,115(3), pp.471-
485.
Grippa P., Letizia E. and Viollet F. forthcoming. “Non-Default Losses at Central Counterparties”
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 34

INTERNATIONAL MONETARY FUND 37Gurley, J. G., and Shaw, E. S. 1960. “Money in a Theory of Finance”. Washington, DC: Brookings Institution.
Harutyunyan, A., and Sánchez Muñoz, C. 2019. “The IMF balance sheet approach: Towards from -whom -to-whom
information on cross -border portfolio securities”. In Are post -crisis statistical initiatives completed? IFC Bulletin
No. 49. Basel: Bank for International Settlements.
Hirshleifer, D., 2015. Behavioral finance. Annual Review of Financial Economics ,7, pp.133-159.
Holmström, B., and J. Tirole. 1998. “Private and Public Supply of Liquidity.” Journal of Political Economy, 106(1), 1-40.
_______. 2011. “Inside and Outside Liquidity”. Cambridge, MA: MIT Press.
Huang, W., Menkveld, A.J. and Yu, S., 2021. Central counterparty exposure in stressed markets. Management
Science ,67(6), pp.3596-3617.
Hüser, A.C., Lepore, C. and Veraart, L.A.M., 2024. How does the repo market behave under stress? Evidence from the
Covid-19 crisis. Journal of Financial Stability ,70, p.101193.
International Monetary Fund (IMF). 2011. Global Financial Stability Report  (April), Chapter 2, “How to Address the
Systemic Part of Liquidity Risk.” Washington, D.C.: International Monetary Fund.
______. 2014a. “Assessing Reserve Adequacy – Specific Proposals:. IMF Policy Paper, 19 December. Washington, DC:
International Monetary Fund
______. 2014b. “2014 Triennial Surveillance Review—Integrating Macrofinancial Surveillance”. IMF Policy Paper.
Washington, DC: International Monetary Fund.
______. 2015. “Balance Sheet Analysis in Fund Surveillance.” IMF Policy Paper. International Monetary Fund,
Washington, D.C.
______. 2016. “Guidance Note on the Assessment of Reserve Adequacy and Related Considerations”. IMF Policy Paper.
Washington, DC: International Monetary Fund.
______. 2020. “United States: Financial Sector Assessment Program—Technical Note on Supervision of Financial
Market Infrastructures, Resilience of Central Counterparties and Innovative Technologies”. IMF Staff Country Report
2020/249. Washington, DC: International Monetary Fund.
______. 2022a. “Review of the Institutional View on the Liberalization and Management of Capital Flows”. IMF Policy
Paper, Volume 2022, Issue 008. Washington, DC: International Monetary Fund
______. 2022b. “Mexico: Financial Sector Assessment Program—Technical Note on Systemic Risk Analysis and Stress
Testing”. IMF Staff Country Report No. 2022/359. Washington, DC: International Monetary Fund
______. 2023. Global Financial Stability Report (April) , Chapter 2. Non-Bank Financial Intermediaries: Vulnerabilities
amid tighter financial conditions. Washington, D.C.: International Monetary Fund.
______. 2025. Global Financial Stability Report (October) , Chapter 1. Shifting Ground beneath the Calm: Stability
Challenges amid Changes in Financial Markets. Washington, D.C.: International Monetary Fund.
International Monetary Fund (IMF) and Financial Stability Board (FSB). 2022. “G20 Data Gaps Initiative (DGI -2): Progress
Achieved, Lessons Learned, and the Way Forward”. Washington, DC: IMF; Basel: FSB. June 9, 2022
International Association of Insurance Supervisors (IAIS). 2025. “Global Insurance Market Report (GIMAR)”, December
2025
©International Monetary Fund. Not for Redistribution 

---

## PDF Sayfa 35

INTERNATIONAL MONETARY FUND 38Jukonis, A., Letizia, E. and Rousová, L., 2022. The impact of derivatives collateralisation on liquidity risk: evidence from
the investment fund sector. ECB Working Paper No. 2756.
Kahneman, D. and Tversky, A. 1979. “Prospect Theory: An Analysis of Decision under Risk”. Econometrica, Vol. 47, No.
2, pp. 263-292.
King, T. B., Nesmith, T. D., Paulson, A., and Prono, T. 2020. “Central Clearing and Systemic Liquidity Risk”. Finance and
Economics Discussion Series No. 2020-009. Board of Governors of the Federal Reserve System
Konaka, Y., Maruyama, T., and Nakamura, F. 2025. “Exploratory Scenario Analysis Considering the Growing Presence of
Domestic and Foreign Investment Funds”. Bank of Japan Working Paper Series No.  25-E-11. Tokyo: Bank of Japan
Lagos, R. 2006. “Inside and Outside Money”. In R. Caplin and A. Schotter (eds.), The Foundations of Positive and
Normative Economics: A Handbook, pp.  179–207. Oxford: Oxford University Press.
Letizia E. and Zhang Y. forthcoming. “Market Impact from Investment Funds Liquidity Distress (MILD)”.
Levels, A., R. de Sousa van Stralen, S. Kroon Patrescu, and I. van Lelyveld. 2018. “CDS Market Structure and Risk
Flows: The Dutch Case.” De Nerderlandsche Bank (DNB) Working Paper No. 592.
Lô, S. and Carpantier, J.F., 2023. “Liquidity Stress Test for Luxembourg Investment Funds: the Time to Liquidation
Approach”. Commission de Surveillance du Secteur Financier (CSSF) Working Paper.
Morris, S., and H.S. Shin. 1998. “Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks.” American Economic
Review , 587-97.
Oura, H. 2022. “Systemwide Liquidity Stress Testing Tool”. IMF Working Paper No. 2022/252. International Monetary
Fund, Washington, D.C
Paddrik, M., S. Rajan, and H.P. Young. 2020. “Contagion in Derivatives Markets.” Management Science , 66(8), 3603-16.
Pinter, G. and Walker D. 2023, “Hedging, market concentration and monetary policy: a joint analysis of gilt and
derivatives exposures”. Bank of England Staff Working Paper No. 1032
Rochet, J.C. and Vives, X., 2004. Coordination failures and the lender of last resort: was Bagehot right after all?. Journal
of the European Economic Association, 2(6), pp.1116-1147.
Shleifer, A. and Vishny, R., 2011. Fire sales in finance and macroeconomics. Journal of economic perspectives ,25(1),
pp.29-48.
Sydow M., Fukke G., Dubiel-Teleszynski T., Franch F., Gallet S., Gründl H., Kotronis S., Miccio D., Pellegrino M.,
Schlütter S. and Sottocornola M. 2024. “Banks and non-banks stressed liquidity shocks and the mitigating role of
insurance companies”. ECB Working Paper No. 3000
Valderrama, L. and Varghese R. 2026. “Risk Propagation in the European Banking System: Amplification Effect from
NBFIs and Market Risks”. IMF Working Paper No. 2026/033. Washington, DC: International Monetary Fund.
©International Monetary Fund. Not for Redistribution 

---
