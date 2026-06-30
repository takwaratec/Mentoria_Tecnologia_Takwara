

Citation: Kolpakov, A.; Dolgov, O.;
Korolskiy, V.; Popov, S.; Anchutin, V.;
Zykov, V. Analysis of Structural
Layouts of Geodesic Dome Structures
with Bar Filler Considering Air
Transportation. Buildings 2022, 12,
242. https://doi.org/10.3390/
buildings12020242
Academic Editor: Pierfrancesco
De Paola
Received: 21 January 2022
Accepted: 16 February 2022
Published: 19 February 2022
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional afﬁl-
iations.
Copyright:
© 2022 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
buildings
Article
Analysis of Structural Layouts of Geodesic Dome Structures
with Bar Filler Considering Air Transportation
Andrey Kolpakov 1,*
, Oleg Dolgov 1, Vladislav Korolskiy 1, Semen Popov 1, Vyacheslav Anchutin 1
and Vadim Zykov 2
1
Moscow Aviation Institute, National Research University, Volokolamskoe Shosse, 4, 125993 Moscow,
Moscow Region, Russia; dolgov@mai.ru (O.D.); korolskijvv@mai.ru (V.K.); semen-popov-2001@mail.ru (S.P.);
vyacheslav.anchutin@mail.ru (V.A.)
2
All-Russian Research Institute for Fire Protection of the Ministry of the Russian Federation for Civil Defence,
Emergencies and Elimination of Consequences of Natural Disasters, mkr. VNIIPO, 12,
143903 Balashikha, Moscow Region, Russia; otdel-15@vniipo.ru
*
Correspondence: a.kolpakov@mai.ru
Abstract: The results are presented from a study of three-layer geodesic dome structures with bar
ﬁllers under their own weight. An algorithm was developed for selecting the type of structural
layout used and the reference parameters chosen in terms of the technological, strength, and weight
characteristics. The results of this analysis aim to make it easier for designers to determine the
optimal reference parameters in the initial stage of the designing of geodetic hemispherical dome
structures, the construction of which is planned to be carried out in remote areas with harsh climatic
conditions. Due to the lack of sufﬁcient ground transport infrastructure, cargo delivery to these
regions is currently possible only with the help of air transport. The importance of this study rests
on the lack of adequate methods for the determination of the reference parameters for geodesic
hemispherical dome structures at an early stage of design. In particular, it is common for the issues
regarding the transportation of structural elements as well as those that involve ensuring the strength
and the technological characteristics of the structure to not be considered simultaneously. This study
owes its relevance to the rapid development of the uninhabited territories of the Russian Federation
in the context of the global ecological crisis caused by anthropogenic impact on the environment.
Keywords: geodesic dome; technological design; structural layout; ﬁnite element method; stress-
strain state; weight analysis
1. Introduction
This article is a continuation of the research cycle devoted to the geodesic dome
structures featured in a previous article that was published in the journal Quality and Life in
December 2021 [1].
The Russian Federation ranks first in the world in terms of its area, which is 17,130,000 km2.
At the same time, only about 12% of this area is mastered, while there are no traces of
human activity in the rest of the territory. As part of the “Strategy for the long-term
development of the Russian Federation with low greenhouse gas emissions until 2050”
project implementation, by 2030, there is a plan to reach a level of carbon emissions equal
to 67% of 1990 levels, and by 2050, to decrease emissions further to 20% of 1990 levels.
At the same time, there is a plan to build new cities in Siberia, which was ofﬁcially
announced by the Minister of Defense of the Russian Federation, S.K. Shoigu, on 5 August
2021. According to this statement, three scientiﬁc and industrial centers with a population
of three hundred thousand to one million people are planned to be built in Siberia between
Bratsk and Krasnoyarsk, as well as in the area of Kansk and Lesosibirsk.
The creation of settlements in the Russian Federation is also considered within the
framework of the comprehensive scientiﬁc and technical program “Connectivity of the
Buildings 2022, 12, 242. https://doi.org/10.3390/buildings12020242
https://www.mdpi.com/journal/buildings

Buildings 2022, 12, 242
2 of 12
territory of the Russian Federation”, selected by the Council for the Priority of Scientiﬁc
and Technological Development.
In the context of these two initiatives, the general task of ensuring the ecological preser-
vation of the territories not affected by anthropogenic impact along with their development
is highlighted.
This area has a sharply continental climate, which can be characterized by a long winter
with a temperature drop as low as −50 ◦C and a short, hot summer with a temperature
high of +30 ◦C. The hot season in the nearest cities lasts from 240 to 250 days a year, and
in summer, there is a high load on the power grid because of the high energy costs of air
conditioning. Thus, one of the steps necessary to achieve this task is to increase the energy
efﬁciency of the capital buildings. Salosina, Alifanov, and Nenerokomov in their work [2]
researched high-porosity open-cell foam in terms of its levels of thermal protection.
It is known that dome buildings in such climatic conditions have up to a one and a half
times higher level of energy efﬁciency when compared to classical rectangular buildings.
In the work of Pogosyan, Strelets, and Vladimirova [3], the communication gap in the
spatial development of the country is highlighted; transport and electronic accessibility is
limited. However, in the work of Lutovinov, Pogosyqn, and Lupyan [4], a solution to the
communication gap is proposed.
The use of dome geodesic structures can provide an alternative solution to this prob-
lem, since this can simplify the rapid construction of reliable long-term shelters without the
need for special construction equipment because of the added possibility of transporting
the assembly elements by air to areas that lack a developed transport infrastructure.
At the same time, reducing the mass of such structures will also signiﬁcantly increase
the maximum range of air transportation. The problems involved in the increasing of the
maximum range of aircraft were previously dealt with by Dolgov and Aruvelli [5].
Additionally, another advantage of these kinds of structures is their high stability
in the event of natural disasters such as earthquakes and hurricanes because of their
geometric shape.
All of these factors taken together allow us to speak about the relevance of a deeper
study of dome structures.
2. Literature Review
A large number of domestic and foreign scientists are currently engaged in research
on the strength and the functional characteristics of dome structures. The current research
was inspired by the work of the following authors:
•
Gritsenko, who was engaged in research on the history of the lattice geodesic dome’s
creation [6].
•
Maria, Esipova, Vintural, and Shabanov, who, in their works, investigated the possibil-
ity of using geodesic domes in various economical ﬁelds [7–10].
•
Granev, Kodysh, Mamin, Bobrov, Reutsu, and Kuznichenko, who studied the existing
lattice structures in terms of their reliability and manufacturability [11].
•
Gorkoltseva, Demidov, Olshanchenko, Shiryaeva, Romanovich, Shanko, Shishkina,
and Kaloshina in their works [12–16] investigated the advantages of dome structures
in comparison to those of classical buildings, according to the criteria of energy
efﬁciency, weight, materials cost, air exchange, seismic resistance, wind resistance, and
environmental friendliness.
•
Zhuravlev, Glushko, and Lakhov in their works [17–20] studied the strength character-
istics of geodetic structural layouts.
•
Lakhova, Gorkoltseva, Miryaeva, and Pilarska in their works [21–24] described various
ways of designing lattice domes.
•
Chepurnenko conducted a comparative analysis of various designs of wavy domes in
order to identify their advantages and disadvantages [25].

Buildings 2022, 12, 242
3 of 12
•
Barbieri, Machado, Barbieri, Lima, Rossot, Guan, Virgin, and Helm calculated the
strength characteristics of dome structures and compared them with the results from
the experimental data [26,27].
•
Jihong, Mingfei, Kaveh, and Talatahari were engaged in the study of dome structures
in terms of their strength characteristics, as well as tasks related to design optimiza-
tion [28,29].
Such a wide interest in the subject of the study, as well as the lack of a comparative
analysis of the varieties of geodesic hemispherical three-layered domes, justiﬁes the rele-
vance of the study. In regions with a mild climate, a single-layer structural layout (Figure 1)
is usually used. Most often, natural materials are used in the structural elements, namely,
the structural frame of the dome structure is made of wooden boards. In such a case, the
geometric characteristics of the thermal insulation material are always limited by the wood
blanks’ parameters.
 
Figure 1. Single-layered dome structure without thermal insulation.
As a rule, standard rectangular boards are chosen as the material of structural frame
elements (Figure 2), which have the following geometric characteristics “L”—length, “h”—
height, and “b”—width.
Figure 2. Geometric characteristics of a rectangular board.
Since, in order to achieve greater structural strength, the boards are positioned in such
a way that the narrow and long side “J” looks out of the structure, there is a limitation on
the thickness of the thermal insulation material layer. The layer thickness cannot exceed
the width “b” of the boards used because it is necessary to install the inner skin to ﬁx it. At
the same time, the use of very wide boards has the potential to signiﬁcantly increase the
cost and mass characteristics of the structure, while the use of more affordable materials
with smaller overall dimensions is more effective.

Buildings 2022, 12, 242
4 of 12
In regions with a harsh climate, where it is necessary to increase the distance between
the external and the internal skin of the dome, multilayer structures are used for laying
thermal insulation material, in which sectional structures are used as structural elements
instead of conventional boards (Figure 3).
 
Figure 3. Geometrical characteristics of the sectional structural element.
In this case, the elements of the inner and outer layers of the dome “X” are connected
using the structural elements in “Y”, which keep the layers at a certain distance, thereby
providing the necessary thickness for holding a thicker layer of thermal insulation material.
An example of such a structural layout is shown in Figure 4.
 
Figure 4. Two-layer geodesic dome structure.
The disadvantage of using such modular structural elements is their low rigidity,
owing to the fact that they are a set of rectangles that have four sides. It is possible to
increase the rigidity by using a structural layout consisting of triangular elements. There are
two variants of geodesic dome structures structural layouts that consist only of triangular
elements. They are known and used in many countries.
3. Materials and Methods
To determine the advantages and the disadvantages of two-layer hemispherical
geodesic dome structural layouts with a triangular structure, a series of strength cal-
culations for different variants using the ﬁnite element method was carried out.
The ﬁnite element method makes it possible to analyze the stress-strain state of
structures with a high degree of accuracy. Aabid, Zakuan, Khan, and Ibrahim [30] claimed
that this method allows the analysis of the structures of different scales, which makes this
method universal.

Buildings 2022, 12, 242
5 of 12
The strength and weight parameters were jointly considered, depending on the amount
of change in the thickness of the bar ﬁller and the number of structural elements.
Four variants of the geodesic domes’ structural layout were considered. The structures
under consideration were spatial three-dimensional three-layer structures consisting of
load-bearing layers in the form of polygonal grids and a bar ﬁller. The structural layouts
under consideration were divided into two types, which were further divided into two
variants. In the ﬁrst type, both bearing layers are polygonal grids consisting of triangles
(Figure 5), and in the second type, the ﬁrst layer consists of triangles and the second of
hexagons (Figure 6). In addition to hexagons, pentagons were also present in the model,
since this condition was necessary for the closure of the dome structure at the pole.
 
Figure 5. First variant of the structural layout.
 
Figure 6. Second variant of the structural layout.
In the ﬁrst type of structure, two variants differ regarding the orientation of the ﬁller.
In the ﬁrst variant of the ﬁrst type of structure (Figure 7), the ﬁller is connected only to
the nodal points of the outer bearing layer, and in the second variant of the ﬁrst type of
structure (Figure 8), the ﬁller is connected to the nodal points of the inner bearing layer. In
the ﬁrst variant of the second type of structure(Figure 9), the layer consisting of triangles
is external, the layer consisting of hexagons is internal, and in the second variant of the
second type of structure (Figure 10), vice versa.
Here are some examples of dome structures, parts of which were transported by air:
•
The metal geodesic dome of the US Antarctic Station Amundsen–Scott is located at
the South Pole of the Earth. It was built in 1975 and used to be the main shelter of the
research station. Its service life in the extreme climatic conditions of the South Pole was
more than 30 years. This dome structure was built from elements premanufactured in
the factory and delivered by air transport.

Buildings 2022, 12, 242
6 of 12
 
Figure 7. Metal geodesic dome of the US Antarctic Station Amundsen–Scott.
 
Figure 8. Geodesic dome of the DYE-2 station of the missile strike early detection system in Greenland.
 
Figure 9. The Lighting dome of the NIISF, outside view.
The geodesic dome of the DYE-2 station of the missile strike early detection system in
Greenland, with a diameter of more than 20 m, the construction of which began in the late
1950s. The construction of this structure was carried out from parts transported exclusively
by air transport.
•
As a close analogue to the ﬁrst type of structure, we may mention the lighting dome of
the Research Institute of Building Physics (NIISF), which was built in Moscow in 1981.
•
As a close analogue to the second type of structure, we may mention the geodesic
dome of the museum dedicated to the environment and water resources in Mon-
treal (Canada), built of steel rods in 1967, with a height of 62 m and a diameter
of 76 m, designed by American engineer and architect Richard Buckminster Fuller
(Figures 11 and 12).

Buildings 2022, 12, 242
7 of 12
 
Figure 10. The Lighting dome of the NIISF, inside view.
 
Figure 11. Montreal “biosphere,” general view.
 
Figure 12. Montreal “biosphere” structure.
The general views of the geodetic hemispherical structural layouts considered are
presented in Figures 13–16.
For each of the four design versions, ten models were created with the division of the
main triangle edge into a different number of structural elements from 2 to 20 in increments
of two. Each structural element is a circular beam with a radius of 20 mm.
Next, a strength analysis of all forty models was carried out with a change in the
distance between the bearing layers from 200 mm to 500 mm in increments of 50 mm. As a
result, 280 calculations were carried out.

Buildings 2022, 12, 242
8 of 12
 
Figure 13. Type 1, variant 1.
 
Figure 14. Type 1, variant 2.
 
Figure 15. Type 2, variant 1.

Buildings 2022, 12, 242
9 of 12
 
Figure 16. Type 2, variant 2.
Strength calculations were carried out using the ﬁnite element method in the Hyper-
Mesh software package in a static solver. Four groups of models were created that differed
in the number of edges per the side of the main triangle from 2 to 20. The model parameters
are given in Table 1.
Table 1. Parameters for FEM models.
Parameter
Value
Dome diameter, m
10
Section view of the structural elements
Circle
Structural elements section radius, mm
20
Material
Steel
Young’s Modulus, MPa
2,100,000
Poisson ratio
0.3
Density, kg/m3
7700
Element type
B31—linear spatial beam ﬁnite element
As mentioned previously, 280 calculations were carried out for each of the models
that was created manually. The use of the highly convenient HyperMesh software package
made it possible to signiﬁcantly reduce the preparation time of the model.
Depending on the geometric division of the main triangle, the number of structural
elements (beams) changed, but regardless of the division, each beam was divided into
10 ﬁnite elements. Thus, the structural elements had the same mesh density. This partition
was dictated primarily by the requirement of mesh convergence.
The ﬁnal elements of the Bar-type, instead of the Rod-type, were used in the model;
the elements of the Bar-type are able to work not only in tension-compression, but also
in bending.
The structure under its own weight was calculated. For this, the gravity acceleration
was set to 9.8 m/s2. As boundary conditions, a restriction on all degrees of freedom for the
lower row of nodes was used, simulating the presence of a foundation.
4. Results and Discussion
The stress-strain state of the structures was estimated by the values of stresses and
displacements. The stress values for all models do not exceed the yield strength of structural
steels. The peak values of the displacements were systemized. Figure 17 shows the
dependences of the displacement values on the mass of the structure and the wall thickness.

Buildings 2022, 12, 242
10 of 12
 
Figure 17. Summary graph of the peak displacements and the mass of the structure on the reference
parameters of the structural layout for geodesic hemispherical two-layer dome structures with a
core ﬁller.
The parameters accepted in the ﬁnite element model correspond to the parameters
that can be used in a real design. Changing the material and the cross-section of structural
elements would yield different results, but this is the topic of another separate study.
In this paper, a comparative analysis of the structural layout of domes was carried out.
After analyzing the graphs in Figure 17, a rational design can be chosen based on the
requirements set.
If the basic requirement is air transportation possibility, then it is advisable to choose a
design that meets all other restrictions with a minimum weight. Judging by the graphs, the
rational choice in this case is a type 2 structure with a division of six elements per main
triangle, since in this case, the displacements of the structure have extremely low values.
The wall thickness should be determined based on the required type of insulation material.
So, when using mineral cotton, the minimum thickness would be 350 mm; at the same time,
when using polyurethane, it is possible to limit the wall thickness to 200 mm.
Similarly, a design selection can be made that is guided by other requirements.

Buildings 2022, 12, 242
11 of 12
Two types of structures have been worked out in two variants. Structures of the second
type have better mass-stiffness characteristics, while structures of the ﬁrst type are better
in terms of their manufacturability. In particular, structures of this type require less labor
intensity during assembly because of the presence of the horizontal rows of the structural
elements. As a result of our calculations, it became possible to quantify the gain in weight
of the second type of structure relative to the ﬁrst one, which allows the designer to make
an optimal choice in favor of a design of one type over another.
5. Conclusions
Based on the dependencies obtained during the analysis of the different variants of
geodesic hemispherical dome structures, an algorithm was determined for selecting a
rational combination of strength and weight characteristics taking into consideration the
limitations associated with manufacturability and the choice of structural materials.
The algorithm developed for the selection of reference parameters during the initial
stage of the design of geodetic hemispherical dome structures may also facilitate the task of
transporting the elements of such structures by air in the future.
The desired outcome of this study is to ensure the possibility of building reliable,
long-term shelters in a short time, with the help of only small groups of workers, and
without the use of special construction equipment, by ensuring a rational combination of
the structural and technological parameters of the structures is used with a minimum mass
of material.
Author Contributions: Conceptualization, A.K.; methodology, O.D.; validation, S.P.; formal analysis,
V.K.; investigation, A.K.; writing—original draft preparation, S.P.; writing—review and editing, V.Z.;
visualization, V.A.; supervision, O.D. All authors have read and agreed to the published version of
the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available on request from the
corresponding author.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Dolgov, O.S.; Dolgova, T.V.; Kolpakov, A.M.; Korolskii, V.V. Ensuring the long-term quality of dome structures based on the use
of lattice high-resource structural layouts of a rational combination of structural and technological parameters with a minimum
mass of material. Qual. Life 2021, 4, 70–77.
2.
Salosina, M.O.; Alifanov, O.M.; Nenarokomov, A.V. An optimal design of thermal protection based on materials morphology.
Comput. Assist. Methods Eng. Sci. 2019, 1, 47–60.
3.
Pogosyan, M.A.; Strelets, D.Y.; Vladimirova, V.G. Territorial Connectivity of the Russian Federation: From the Statement of
Complex Problems to Drawing up Integrated Scientiﬁc and Technical Projects. Her. Russ. Acad. Sci. 2019, 89, 179–184. [CrossRef]
4.
Lutovinov, A.A.; Lupyan, E.A.; Pogosyan, M.A.; Shemyakov, A.O. Providing Information Connectivity over Russian Territory
Using Remote Sensing Systems of the Earth. Her. Russ. Acad. Sci. 2019, 89, 190–195. [CrossRef]
5.
Dolgov, O.S.; Aruvelli, S.V. A Method of Increasing the Electric Aircraft Flight Range by Reducing Weight during Flight. Russ.
Aeronaut. 2020, 63, 405–412.
6.
Gritsenko, D.A. Fuller and his geodesic domes. In Science, Education and Experimental Design; Abstracts of the International
Scientiﬁc and Practical Conference of Teaching Staff, Young Scientists and Students; Moscow Architectural Institute (State
Academy): Moscow, Russia, 2014; p. 407.
7.
Vrontissi, M.K. Designing and building a geodesic dome as a bearing structure for an ‘artiﬁcial sky’ ligthting installation. In
Proceedings of the Evolution and Trends in Design, Analysis and Construction of Shell and Spatial Structures [International
Association for Shell and Spatial Structures (IASS) Symposium 2009], Valencia, Spain, 1 March 2009.
8.
Esipova, A.A. Application of geodesic domes in construction: Advantages and disadvantages. North Caucasus Branch of
Belgorod State Technological University named after V.G. Shukhov, Mineralnye Vody. Sci. Mod. 2015, 38, 8–11.

Buildings 2022, 12, 242
12 of 12
9.
Vintural, D.A. Structures on Mars. Actual problems of aviation and cosmonautics. In Proceedings of the Materials of the VI
International Scientiﬁc and Practical Conference Dedicated to the Cosmonautics Day, Tomsk, Russia, 6 April 2020; pp. 275–276.
10.
Shabanov, Y.S. Application of dome construction technology in the construction of low-rise residential buildings. In Generation of
the Future: The View of Young Scientists—2020 Kursk; Don State Technical University: Rostov-on-Don, Russia, 2020; pp. 381–383.
11.
Granev, V.V.; Kodysh, E.N.; Mamin, A.N.; Bobrov, V.V.; Reutsu, A.V.; Kuznechenko, S.A. Preservation of the Shukhov Radio
Tower—Current state and prospects. In Proceedings of the Collection of Scientiﬁc Works of the RAASN “Fundamental, Ex-
ploratory and Applied Research on Scientiﬁc Support for the Development of Architecture, Urban Planning and the Construction
Industry of the Russian Federation”, Moscow, Russia, 4 April 2018.
12.
Gorkoltseva, D.S. Research and development of an energy-efﬁcient dome structure. Tomsk State University of Architecture and
Civil Engineering, Russia, Tomsk. Prospects for the Development of Fundamental Sciences. In Proceedings of the scientiﬁc papers
of the XII International Conference of Students and Young Scientists, Tomsk, Russia, 21–24 April 2015; pp. 1263–1265.
13.
Panova, Y.V.; Demidov, S.V. Effective construction system—Geodesic dome. In Proceedings of the Collection: Cherepovets
Scientiﬁc Readings—2014 Materials of the All-Russian Scientiﬁc and Practical Conference, Cherepovets, Russia, 3–5 November
2015; pp. 39–43.
14.
Olshanchenko, A.A.; Shiryaeva, N.P. Energy saving in domed houses. In Proceedings of the Collection: Energy and Resource
Conservation. Energy Supply. Unconventional and Renewable Energy Sources, Materials of the International Scientiﬁc and
Practical Conference of Students, postgraduates and Young Scientists Dedicated to the Memory of Professor N.I. Danilov (1945–
2015)—Danilov Readings. Ministry of Education and Science of the Russian Federation, Ural Federal University Named after the
First President of Russia B. N. Yeltsin. Ekaterinburg, Russia, 11–15 December 2017; pp. 299–303.
15.
Romanovich, A.N. Geodesic domes. general information. features of application and calculation. Mod. Innov. 2016, 6, 22–23.
16.
Shanko, P.S.; Shishkina, A.V.; Kaloshina, S.V. Construction methods and advantages of domed buildings. Mod. Technol. Constr.
Theory Pract. 2016, 2, 341–348.
17.
Zhuravlev, A.A. Snapping the bar structure of lattice dome in the form of a 980-agon. News Univ. Constr. Archit. 1983, 6, 34–39.
18.
Glushko, K.K. Study of shape stability of rod polyhedra of lattice domes. In Proceedings of the II International Scientiﬁc and
Technical Conference “Theory and Practice of Research and Design in Construction Using Computer-Aided Design (CAD)
Systems”, Moscow, Russia, 25–26 October 2018; pp. 33–42.
19.
Glushko, K.K. Loss of local stability of lattice domes with rigid nodes. In Proceedings of the II International Scientiﬁc and
Technical Conference “Theory and Practice of Research and Design in Construction Using Computer-Aided Design (CAD)
Systems”, Brest, Belarus, 29–30 March 2018; pp. 24–33.
20.
Lakhov, A.Y. Approximate method for determining the maximum tensile stresses in the rods of double-circuit geodesic domes of
the “R” system from the impact of its own weight. Bull. MGSU 2014, 1, 58–65.
21.
Lakhov, A.Y. Two-contour geodesic shells with pentahedral pyramids. Nizhny Novgorod State University of Architecture and
Civil Engineering. Eng. Bull. Don 2019, 6, 18.
22.
Gorkoltseva, D.S. Design calculation and construction of a geodesic dome model. In Proceedings of the 1 Tomsk State University
of Architecture and Civil Engineering, Tomsk Youth Scientiﬁc Potential of the XXI Century: Stages of Cognition, Tomsk, Russia,
25–28 April 2017; pp. 70–74.
23.
Miryaev, B.V. Optimization of the geometric scheme of lattice domes formed on the basis of an icosahedron. Reg. Archit. Constr.
2012, 3, 122–125.
24.
Pilarska, D. Two subdivision methods based on the regular octahedron for single-and double-layer spherical geodesic domes. Int.
J. Space Struct. 2020, 35, 160–173. [CrossRef]
25.
Chepurnenko, A.S.; Kochura, V.G.; Saibel, A.V. Finite element analysis of the stress-strain state of wavy shells. Constr. Technog.
Saf. 2018, 11, 27–31.
26.
Barbieri, N.; Machado, R.D.; Barbieri, L.S.V.; Lima, K.F.; Rossot, D. Dynamic Behavior of the Geodesic Dome Joints. Int. J. Comput.
Appl. 2016, 40, 40–44. [CrossRef]
27.
Guan, Y.; Virgin, L.N.; Helm, D. Structural behavior of shallow geodesic lattice domes. Int. J. Solids Struct. 2018, 15515, 225–239.
[CrossRef]
28.
Ye, J.; Lu, M. Optimization of domes against instability. Steel Compos. Struct. 2018, 28, 427–438.
29.
Kaveh, A.; Talatahari, S. Geometry and topology optimization of geodesic domes using charged system search. Struct. Multidiscip.
Optim. 2011, 43, 215–229. [CrossRef]
30.
Aabid, A.; Zakuan, M.A.M.B.M.; Khan, S.A.; Ibrahim, Y.E. Structural analysis of three-dimensional wings using ﬁnite element
method. Aerosp. Syst. 2021, 3, 1–17. [CrossRef]
