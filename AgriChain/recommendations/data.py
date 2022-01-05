

def crop(crop_name):
    crop_data = {
    "apple":["Apple Crop", "/static/images/crop/apple.jpg", "rabi","Sri Lanka, United Arab Emirates, Taiwan"],
    "paddy":["/static/images/paddy.jpg", "W.B., U.P., Andhra Pradesh, Punjab, T.N.", "kharif","Bangladesh, Saudi Arabia, Iran"],
    "barley":["/static/images/barley.jpg", "Rajasthan, Uttar Pradesh, Madhya Pradesh, Haryana, Punjab", "rabi","Oman, UK, Qatar, USA"],
    "maize":["/static/images/maize.jpg", "Karnataka, Andhra Pradesh, Tamil Nadu, Rajasthan, Maharashtra", "kharif", "Hong Kong, United Arab Emirates, France"],
    "bajra":["/static/images/bajra.jpg", "Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat", "kharif", "Oman, Saudi Arabia, Israel, Japan"],
    "copra":["/static/images/copra.jpg", "Kerala, Tamil Nadu, Karnataka, Andhra Pradesh, Orissa, West Bengal","rabi", "Veitnam, Bangladesh, Iran, Malaysia"],
    "cotton":["/static/images/cotton.jpg", "Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat","rabi", " China, Bangladesh, Egypt"],
    "masoor":["/static/images/masoor.jpg", "Uttar Pradesh, Madhya Pradesh, Bihar, West Bengal, Rajasthan", "rabi", "Pakistan, Cyprus,United Arab Emirates"],
    "gram":["/static/images/gram.jpg", "Madhya Pradesh, Maharashtra, Rajasthan, Uttar Pradesh, Andhra Pradesh & Karnataka", "rabi", "Veitnam, Spain, Myanmar"],
    "groundnut":["/static/images/groundnut.jpg", "Andhra Pradesh, Gujarat, Tamil Nadu, Karnataka, and Maharashtra", "kharif", "Indonesia, Jordan, Iraq"],
    "arhar":["/static/images/arhar.jpg", "Maharashtra, Karnataka, Madhya Pradesh and Andhra Pradesh", "kharif", "United Arab Emirates, USA, Chicago"],
    "sesamum":["/static/images/sesamum.jpg", "Maharashtra, Rajasthan, West Bengal, Andhra Pradesh, Gujarat", "rabi", "Iraq, South Africa, USA, Netherlands"],
    "jowar":["/static/images/jowar.jpg", "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Gujarat", "kharif", "Torronto, Sydney, New York"],
    "moong":["/static/images/moong.jpeg", "Rajasthan, Maharashtra, Andhra Pradesh", "rabi", "Qatar, United States, Canada"],
    "niger":["/static/images/niger.jpg", "Andha Pradesh, Assam, Chattisgarh, Gujarat, Jharkhand", "kharif", "United States of American,Argenyina, Belgium"],
    "rape":["/static/images/rape.jpg", "Rajasthan, Uttar Pradesh, Haryana, Madhya Pradesh, and Gujarat", "rabi", "Veitnam, Malaysia, Taiwan"],
    "jute":["/static/images/jute.jpg", " West Bengal , Assam , Orissa , Bihar , Uttar Pradesh", "kharif", "JOrdan, United Arab Emirates, Taiwan"],
    "safflower":["/static/images/safflower.jpg",  "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Orissa", "kharif", " Philippines, Taiwan, Portugal"],
    "soyabean":["/static/images/soyabean.jpg",  "Madhya Pradesh, Maharashtra, Rajasthan, Madhya Pradesh and Maharashtra", "kharif", "Spain, Thailand, Singapore"],
    "urad":["/static/images/urad.jpg",  "Andhra Pradesh, Maharashtra, Madhya Pradesh, Tamil Nadu", "rabi", "United States, Canada, United Arab Emirates"],
    "ragi":["/static/images/ragi.jpg",  "Maharashtra, Tamil Nadu and Uttarakhand", "kharif", "United Arab Emirates, New Zealand, Bahrain"],
    "sunflower":["/static/images/sunflower.jpg",  "Karnataka, Andhra Pradesh, Maharashtra, Bihar, Orissa", "rabi", "Phillippines, United States, Bangladesh"],
    "sugarcane":["/static/images/sugarcane.jpg","Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh" , "kharif", "Kenya, United Arab Emirates, United Kingdom"]
    }
    return crop_data[crop_name]




def crop(crop_name):
    fertilizer_data = {
    "wheat":["/static/images/wheat.jpg", "U.P., Punjab, Haryana, Rajasthan, M.P., bihar", "rabi","Sri Lanka, United Arab Emirates, Taiwan"],
    "paddy":["/static/images/paddy.jpg", "W.B., U.P., Andhra Pradesh, Punjab, T.N.", "kharif","Bangladesh, Saudi Arabia, Iran"],
    "barley":["/static/images/barley.jpg", "Rajasthan, Uttar Pradesh, Madhya Pradesh, Haryana, Punjab", "rabi","Oman, UK, Qatar, USA"],
    "maize":["/static/images/maize.jpg", "Karnataka, Andhra Pradesh, Tamil Nadu, Rajasthan, Maharashtra", "kharif", "Hong Kong, United Arab Emirates, France"],
    "bajra":["/static/images/bajra.jpg", "Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat", "kharif", "Oman, Saudi Arabia, Israel, Japan"],
    "copra":["/static/images/copra.jpg", "Kerala, Tamil Nadu, Karnataka, Andhra Pradesh, Orissa, West Bengal","rabi", "Veitnam, Bangladesh, Iran, Malaysia"],
    "cotton":["/static/images/cotton.jpg", "Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat","rabi", " China, Bangladesh, Egypt"],
    "masoor":["/static/images/masoor.jpg", "Uttar Pradesh, Madhya Pradesh, Bihar, West Bengal, Rajasthan", "rabi", "Pakistan, Cyprus,United Arab Emirates"],
    "gram":["/static/images/gram.jpg", "Madhya Pradesh, Maharashtra, Rajasthan, Uttar Pradesh, Andhra Pradesh & Karnataka", "rabi", "Veitnam, Spain, Myanmar"],
    "groundnut":["/static/images/groundnut.jpg", "Andhra Pradesh, Gujarat, Tamil Nadu, Karnataka, and Maharashtra", "kharif", "Indonesia, Jordan, Iraq"],
    "arhar":["/static/images/arhar.jpg", "Maharashtra, Karnataka, Madhya Pradesh and Andhra Pradesh", "kharif", "United Arab Emirates, USA, Chicago"],
    "sesamum":["/static/images/sesamum.jpg", "Maharashtra, Rajasthan, West Bengal, Andhra Pradesh, Gujarat", "rabi", "Iraq, South Africa, USA, Netherlands"],
    "jowar":["/static/images/jowar.jpg", "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Gujarat", "kharif", "Torronto, Sydney, New York"],
    "moong":["/static/images/moong.jpeg", "Rajasthan, Maharashtra, Andhra Pradesh", "rabi", "Qatar, United States, Canada"],
    "niger":["/static/images/niger.jpg", "Andha Pradesh, Assam, Chattisgarh, Gujarat, Jharkhand", "kharif", "United States of American,Argenyina, Belgium"],
    "rape":["/static/images/rape.jpg", "Rajasthan, Uttar Pradesh, Haryana, Madhya Pradesh, and Gujarat", "rabi", "Veitnam, Malaysia, Taiwan"],
    "jute":["/static/images/jute.jpg", " West Bengal , Assam , Orissa , Bihar , Uttar Pradesh", "kharif", "JOrdan, United Arab Emirates, Taiwan"],
    "safflower":["/static/images/safflower.jpg",  "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Orissa", "kharif", " Philippines, Taiwan, Portugal"],
    "soyabean":["/static/images/soyabean.jpg",  "Madhya Pradesh, Maharashtra, Rajasthan, Madhya Pradesh and Maharashtra", "kharif", "Spain, Thailand, Singapore"],
    "urad":["/static/images/urad.jpg",  "Andhra Pradesh, Maharashtra, Madhya Pradesh, Tamil Nadu", "rabi", "United States, Canada, United Arab Emirates"],
    "ragi":["/static/images/ragi.jpg",  "Maharashtra, Tamil Nadu and Uttarakhand", "kharif", "United Arab Emirates, New Zealand, Bahrain"],
    "sunflower":["/static/images/sunflower.jpg",  "Karnataka, Andhra Pradesh, Maharashtra, Bihar, Orissa", "rabi", "Phillippines, United States, Bangladesh"],
    "sugarcane":["/static/images/sugarcane.jpg","Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh" , "kharif", "Kenya, United Arab Emirates, United Kingdom"]
    }
    return fertilizer_data[fertilizer_name]







import appleImage from "main/static/images/crop/apple.jpg"
import bananaImage from "main/static/images/crop/banana.jpg"
import blackgramImage from "../main/static/images/crop/blackgram.jpg"
import chickpeaImage from "main/static/images/crop/chickpea.jpg"
import coconutImage from "main/static/images/crop/coconut.jpg"
import coffeeImage from "main/static/images/crop/coffee.png"
import cottonImage from "main/static/images/crop/cotton.png"
import grapesImage from "main/static/images/crop/grape.png"
import juteImage from "main/static/images/crop/jute.jpg"
import kidneybeansImage from "main/static/images/crop/kidneybeans.jpg"
import lentilImage from "main/static/images/crop/lentil.jpg"
import maizeImage from "main/static/images/crop/maize.jpg"
import mangoImage from "main/static/images/crop/mango.jpg"
import mothbeansImage from "main/static/images/crop/mothbean.jpg"
import mungbeanImage from "main/static/images/crop/mungbean.jpg"
import muskmelonImage from "main/static/images/crop/muskmelon.jpg"
import orangeImage from "main/static/images/crop/orange.jpg"
import papayaImage from "main/static/images/crop/papaya.jpg"
import pigeonpeasImage from "main/static/images/crop/pigeonpeas.jpg"
import pomegranateImage from "main/static/images/crop/pomogranate.jpg"
import riceImage from "main/static/images/crop/rice.jpg"
import watermelonImage from "main/static/images/crop/watermelon.jpg"

import fert143514Image from "main/static/images/fertilizer/fert143514.png"
import fert2828Image from "main/static/images/fertilizer/fert2828.jpg"
import fert171717Image from "main/static/images/fertilizer/fert171717.jpg"
import fert2020Image from "main/static/images/fertilizer/fert2020.jpg"
import fert102626Image from "main/static/images/fertilizer/fert102626.png"
import ureaFertImage from "main/static/images/fertilizer/ferturea.jpg"
import dapFertImage from "main/static/images/fertilizer/fertdap.jpg"



cropData = {
    apple:{
        title:"Apple Crop",
        imageUrl:appleImage,
        description: "Normally the apples are ready for harvest from September-October except in the Nilgiris where the season is from April to July. The fruits mature within 130-150 days after the full bloom stage depending upon the variety grown. The ripening of fruits is associated with the change in colour, texture, quality and the development of the characteristic flavour. The fruits at the time of harvest should be uniform, firm and crisp. The colour of the skin at maturity ranges from yellow-red depending on the variety. However, the optimum time of harvest depends on fruit quality and intended period of storage. Due to the introduction of dwarf rootstock hand picking is recommended as it reduces bruising due to fruit fall during mechanical harvesting."
    },
    banana:{
        title:"Bana Crop",
        imageUrl:bananaImage,
        description: "Banana is harvested when the fruit is slightly or fully mature depending on the market preferences. For long distance transportation, harvesting is done at 75-80 % maturity.  The fruit is climacteric and can reach consumption stage after ripening operation. The planted crop gets ready for harvest within 12-15 months of planting and the main harvesting season of banana is from September to April.  Bunches attain maturity from 90-150 days after flowering depending upon variety, soil, weather condition and elevation. Bunch should be harvested when fingers of second hand from top are 3/4 rounded with the help of sharp sickle 30cm above the first hand. Harvest may be delayed upto 100-110 days after opening of the first hand. Harvested bunch should generally be collected in well padded tray or basket and brought to collection site. Bunches should be kept out of light after harvest, since this hastens ripening and softening. For local consumption, hands are often left on stalks and sold to retailers."        
    },
    blackgram:{
        title:"Blackgram Crop",
        imageUrl:blackgramImage,
        description:"Urd should be harvested when 70-80 % pods matured and most of the pods turn black. Over maturity may result in shattering. Harvested crop should be dried on threshing floor for few days and then threshed. Threshing can be done either manually or by trampling under the feet of bullocks. The clean seeds should be sun dried for 3 - 4 days to bring their moisture content at 8-10% to safely store in appropriate bins."
    },
    chickpea:{
        title:"ChickPea Crop",
        imageUrl:chickpeaImage,
        description:"The plant grows to 20–50 cm (8–20 in) high and has small, feathery leaves on either side of the stem. Chickpeas are a type of pulse, with one seedpod containing two or three peas. It has white flowers with blue, violet, or pink veins. Several varieties of chickpea are cultivated throughout the world. Desi chana closely resembles both seeds found on archaeological sites and the wild plant ancestor of domesticated chickpeas. Cicer reticulatum only grows in southeast Turkey, where chickpeas are believed to have originated."
    },
    coconut:{
        title:"Coconut Crop",
        imageUrl:coconutImage,
        description:"Coconut palms are normally cultivated in hot and wet tropical climates. They need year round warmth and moisture to grow well and fruit. Coconut palms are hard to establish in dry climates, and cannot grow there without frequent irrigation; in drought conditions, the new leaves do not open well, and older leaves may become desiccated; fruit also tends to be shed."
    },
    coffee:{
        title:"Coffee Crop",
        imageUrl:coffeeImage,
        description:"The traditional method of planting coffee is to place 20 seeds in each hole at the beginning of the rainy season. This method loses about 50% of the seeds' potential, as about half fail to sprout. A more effective process of growing coffee, used in Brazil, is to raise seedlings in nurseries that are then planted outside at six to twelve months. Coffee is often intercropped with food crops, such as corn, beans, or rice during the first few years of cultivation as farmers become familiar with its requirements. Coffee plants grow within a defined area between the tropics of Cancer and Capricorn, termed the bean belt or coffee belt."
    },
    cotton:{
        title:"Cotton Crop",
        imageUrl:cottonImage,
        description:"Successful cultivation of cotton requires a long frost-free period, plenty of sunshine, and a moderate rainfall, usually from 60 to 120 cm (24 to 47 in)[citation needed]. Soils usually need to be fairly heavy, although the level of nutrients does not need to be exceptional. In general, these conditions are met within the seasonally dry tropics and subtropics in the Northern and Southern hemispheres, but a large proportion of the cotton grown today is cultivated in areas with less rainfall that obtain the water from irrigation. Production of the crop for a given year usually starts soon after harvesting the preceding autumn."
    },
    grapes:{
        title:"Grapes Crop",
        imageUrl:grapesImage,
        description:"Harvesting period for grapes, generally starts 30-70 days after fruit set, by the time berries change color from green to yellow (for white varieties), or red-purple (for red varieties). During this stage, we normally have an increase in sugars and a decrease in acids inside the fruits. In general, in the northern hemisphere, most varieties mature from August since November, while in the southern hemisphere from March to August."
    },
    jute:{
        title:"Jute Crop",
        imageUrl:juteImage,
        description:"To grow jute, farmers scatter the seeds on cultivated soil. When the plants are about 15–20 cm tall, they are thinned out. About four months after planting, harvesting begins. The plants are usually harvested after they flower, before the flowers go to seed. The stalks are cut off close to the ground. The stalks are tied into bundles and soaked in water for about 20 days. This process softens the tissues and breaks the hard [pectin] bond between the bast and [Jute hurd] (inner woody fiber stick) and the process permits the fibres to be separated. The fibres are then stripped from the stalks in long strands and washed in clear, running water."
    },
    kidneybeans:{
        title:"Kidney Beans Crop",
        imageUrl:kidneybeansImage,
        description:"Harvest when pods are full grown and ripe and there color turn to yellow. Also leaves turn yellow and majority of leaves drop. Depending upon variety use pods are ready to harvest 7-12 days after flowering. Overall crop is ready to harvest in 120-130 days. Do harvesting at right time as delay cause shattering. Keep harvested plant for three-four days in sun. After proper drying of crop, threshing is done with help of bullocks or with sticks."
    },
    lentil:{
        title:"Lentil Crop",
        imageUrl:lentilImage,
        description:"Harvest lentils when the plant begin to turn yellow and the pods become brown. Lentils are commonly used as dry beans or peas. For dried seeds, harvest pods when they have matured and hardened. Leave lentils unshelled until you are ready to use them. Dried lentils are ready for harvest 110 days after sowing. Lentil also can be used as snap beans; harvest these green about 70 to 80 days after sowing."
    },
    maize:{
        title:"Maize Crop",
        imageUrl:maizeImage,
        description:"The ears are removed from the standing plants and they are piled to open for twenty four hours and they are spread for drying in the sun. In this method stalks may be used as green fodder. The plants are cut and piled up in the shade and the cobs are removed after two or three days of harvesting. The dried plants are used for haymaking. Maize grown for fodder are harvested at the milk to early dough stage. The earlier harvested crop usually yields less and is poor in protein content. For silage making late dough stage is preferred."
    },
    mango:{
        title:"Mango Crop",
        imageUrl:mangoImage,
        description:"In western India, mango puts forth three growth flushes, the first are in the early spring (FebruaryMarch), the second during March-April and the third in the beginning of winter (October-November). In Bihar, the first growth noticed in early spring, the second in April-May and the third in July-August. In UP, only two flushes are produced, in March-April and July-August. In Punjab, as many as five flushes are produced from April-August. April and Mayflushes being found most heavy. In South India, mango usually gives two growth flushes, one in February-June and the other in October-November. In mango about 8-10 months old shoots under certain conditions cease to grow at least 4 months prior to blossoming. These shoots are capable of producing flower buds. Other shoots, which appear in subsequent flushes during late monsoon, do not come to flowering. These shoots flower during the next season after accumulating sufficient metabolites necessary for fruit-bud differentiation. Thus the fruits will be ready for harvest in April-May from a plant flowered during October-November."
    },
    mothbeans:{
        title:"Mothbeans Crop",
        imageUrl:mothbeansImage,
        description:"The moth bean plants generally take between 75 and 90 days from planting to harvesting. Harvesting moth bean is pretty difficult, and it’s the main drawback to this crop. You have to cut the plants with a sickle, because you can’t use mowers mainly due to the shape and density of the moth bean’s branches. Then after cutting, it is threshed and winnowed after being dried for approximately one week."
    },
    mungbean:{
        title:"Mungbean Crop",
        imageUrl:mungbeanImage,
        description:"The olive-green mung beans should be harvested in the field after their pods have dried, typically in early to mid-September. Farmers use the same type of combine machinery used to harvest soybeans, but because mung beans are smaller than soybeans, they adjust the combine settings and screen size for the smaller bean size. Mung beans should be cleaned of debris before storage, and the beans should have no more than 12 percent moisture content for storage. Because harvested beans may be sprouted and eaten directly, stored beans should not be treated with fungicides, insecticides or bactericides."
    },
    muskmelon:{
        title:"Muskmelon Crop",
        imageUrl:muskmelonImage,
        description:"Many muskmelons and cantaloupes separate naturally from the stem when the melons are ripe, so they come away from the vine with only a gentle tug. Melons that do not “slip” often sound hollow when tapped, and the skin color takes on a yellowish cast. Wipe harvested melons clean and store indoors in a cool place, or in the refrigerator."
    },
    orange:{
        title:"Orange Crop",
        imageUrl:orangeImage,
        description:"Canopy-shaking mechanical harvesters are being used increasingly in Florida to harvest oranges. Current canopy shaker machines use a series of six-to-seven-foot-long tines to shake the tree canopy at a relatively constant stroke and frequency."
    },
    papaya:{
        title:"Papaya Crop",
        imageUrl:papayaImage,
        description:"Fruits are harvested when they are of full size, light green in colour with tinge of yellow at apical end. On ripening, fruits of certain varieties turn yellow while some of them remain green. When the latex ceases to be milky and become watery, the fruits are suitable for harvesting. The economic life of papaya plant is only 3 to 4 years.  The yield varies widely according to variety, soil, climate and management of the orchard. The yield of 75-100 tonnes /ha. is obtained in a season from a papaya orchard depending on spacing and cultural practices."
    },
    pigeonpeas:{
        title:"Pigeon Peas Crop",
        imageUrl:pigeonpeasImage,
        description:"With two third to three fourth pods at maturity judged by changing their colour to brown is the best harvesting time. The plants are usually cut with a sickle within 75 cm above the ground. Harvested plants should be left in the field for sun drying for 3-6 days depending on season. Threshing is done either by beating the pods with stick or using Pullman thresher. The proportion of seed to pods is generally 50 - 60%. The clean seeds should be sun dried for 3-4 days to bring their moisture content at 9-10% to safely store in appropriate bins."
    },
    pomegranate:{
        title:"Pomegranate Crop",
        imageUrl:pomegranateImage,
        description:"Pomegranate being a non-climacteric fruit should be picked when fully ripe. Pomegranate plants take 4-5 years to come into bearing.  Harvesting of immature or over mature fruits affects the quality of the fruits. The fruits become ready for picking 120-130 days after fruit set. The calyx at the distal end of the fruit gets closed on maturity. At maturity, the fruits turn yellowish-red and get suppressed on sides."
    },
    rice:{
        title:"Rice Crop",
        imageUrl:riceImage,
        description:"Harvesting is the process of collecting the mature rice crop from the field. Depending on the variety, a rice crop usually reaches maturity at around 105–150 days after crop establishment. Harvesting activities include cutting, stacking, handling, threshing, cleaning, and hauling. Good harvesting methods help maximize grain yield and minimize grain damage and deterioration."
    },
    watermelon:{
        title:"Watermelon Crop",
        imageUrl:watermelonImage,
        description:"Watermelons will be ready for harvest 65 to 90 days after sowing depending on the variety. When watermelons are ready to harvest vine tendrils will begin to turn brown and die off. If the tendrils are green the melon is not ripe. A ripe watermelon will make a dull hollow sound when thumped. The soil-side of a watermelon will turn from white to pale yellow when the fruit is ready for harvest. Ripe melons will have a sweet aroma at the stem end. Limit water for a week in advance of the harvest to concentrate sweetness. Watermelons on a single plant will all be ready for harvest over a two week period."
    }
}


fertilizerData = {
    Urea:{
        title:"Urea Fertilizer",
        imageUrl:ureaFertImage,
        description: "The agricultural industry widely uses urea, a white crystalline solid containing 46 percent nitrogen as an animal feed additive and fertilizer. Here, we'll focus on its role as a nitrogen fertilizer. In the past decade, urea has surpassed and nearly replaced ammonium nitrate as a fertilizer."
    },
    DAP:{
        title:"DAP Fertilizer",
        imageUrl:dapFertImage,
        description: "Di-ammonium Phosphate popularly known as DAP is a preferred fertilizer in India because it contains both Nitrogen and Phosphorus which are primary macro-nutrients and part of 18 essential plant nutrients. DAP is manufactured by reacting Ammonia with Phosphoric acid under controlled conditions in fertilizer plants."
    },
    "14-35-14":{
        title:"14-35-14 Fertilizer",
        imageUrl:fert143514Image,
        description:"GROMOR 14-35-14 is a complex fertiliser containing all major nutrients viz. Nitrogen, Phosphorous and Potassium. The only complex having highest total nutrient content among the NPK complex fertilisers. (Total nutrients are 63%)."
    },
    "28-28":{
        title:"28-28 Fertilizer",
        imageUrl:fert2828Image,
        description:"This is the highest Nitrogen-containing Complex fertilizer with 28%. 19% of Nitrogen is in Urea form and 9% is in Ammonical form. Ammonium Phosphate is coated over Urea prill, due to which the losses from Urea will be minimized. 25.2% out of 28% Phosphate is in water-soluble form and easily available to plants."
    },
    "17-17-17":{
        title:"17:17:17 Fertilizer",
        imageUrl:fert171717Image,
        description:"N-P-K 17-17-17 Fertilizer is a complex fertilizer containing all three major plant nutrient ,Nitrogen,Phosphorous.Potassium in equal proportion .contain nitrogen ,phosphorous.potassium in 17:17:17 combination.it also helps regulate metabolic activities n-p-k 17-17-17 fertilizers are water soluble and can be taken up by the plant almost immediately an all purpose 17-17-17 fertilizer will provide the nutrients all plants need for healthy growth.All parts of plants need nitrogen for growth -the roots leaves,stems, flowers and fruits.Nitrogen gives plants their green color and is needed to form protein. A lack of nitrogen causes the lower leaves to turn yellow and the whole plant to turn pale green.Phosphorous is needed for cell division and help form roots flowers and fruits.Phosphorous deficiency causes stunted growth and poor flowering and fruiting.Potassium is important for regulation of water and nutrient movement in plant cells, there by promoting fruiting ,flowering, hardiness and promote the overall health of the plant by providing resistance to diseases. A Potassium shortage show up in various ways but stun growth and yellowish lower leaves.Usage Instruction:seeds and seedling stage use 1/4 tsp to 1 liter water.After 3-4 true leaves stage use 1/2 tsp to 1 liter water . blooming stage use 2/3 tsp n-p-k to 1 liter water."
    },
    "20-20":{
        title:"20-20 Fertilizer",
        imageUrl:fert2020Image,
        description:"GROMOR 20-20-0-13 is Ammonium Phosphate Sulphate containing Nitrogen and Phosphate in 1:1 ratio. It contains 20% Nitrogen. Of this 90% of Nitrogen is present in Ammonical form and the rest in Amide form. However, the entire Nitrogen is available to crops in Ammonical form. It contains 20% Phosphate, 85% of which is present in water-soluble form and is effectively and easily available to crops. It contains 15% Sulphur which is the 4th major nutrient after NPK. Sulphur response in many crops has been reported very encouraging and application of GROMOR 20-20-0-13 will supplement the Sulphur requirement of crops. It is granular in nature and can be easily applied by broadcasting, placement or drilling. Hygroscopic nature is much less and it is suitable to a variety of soils and crops. It is an excellent fertilizer for all crops grown in Sulphur deficient soils and is highly suitable for Sulphur loving crops such as Oilseeds."
    },
    "10-26-26":{
        title:"10-26-26 Fertilizer",
        imageUrl:fert102626Image,
        description:"GROMOR 10:26:26 is a complex fertilizer containing all the three major plant nutrients viz. Nitrogen, Phosphorous and Potassium. GROMOR 10:26:26 contains Phosphorous and Potassium in the ratio of 1:1, the highest among the NPK fertilizers. It contains 7% Nitrogen in the Ammonical form, 22% out of 26% phosphate in the water-soluble form and the entire 26% potash is available in the water-soluble form. GROMOR 10:26:26 is ideally suitable for crops which require high phosphate and potassium and this grade is very popular among the Sugarcane farmers of Maharashtra, Karnataka and Andhra Pradesh and Potato farmers of West Bengal & Uttar Pradesh. GROMOR 10:26:26 is also suitable for Fruit crops."
    }
}