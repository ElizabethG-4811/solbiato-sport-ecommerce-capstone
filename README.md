# Solbiato Sport Streetwear: The E-Commerce Evolution of a D.C. Streetwear Icon
### Data Analytics Capstone | Developed by Elizabeth Green

---

## Table of Contents
* [1. Project Overview & Inspiration](#1-project-overview--inspiration)
* [2. The Georgetown Storefront History](#2-the-georgetown-storefront-history)
* [3. Business Research Question](#3-business-research-question)
* [4. Digital Search Volatility Analysis](#4-digital-search-volatility-analysis)
* [5. Annual Search Volatility Breakdown](#5-annual-search-volatility-breakdown)
* [6. Retail Challenges in Georgetown](#6-retail-challenges-in-georgetown)
* [7. Commercial Real Estate Trends](#7-commercial-real-estate-trends)
* [8. The Product Catalog Dashboard](#8-the-product-catalog-dashboard)
* [9. The Three-Step Business Strategy](#9-the-three-step-business-strategy)
* [10. Website Inventory Data & Code Structure](#10-website-inventory-data--code-structure)
* [11. Price Brackets & Profit Margins](#11-price-brackets--profit-margins)
* [12. Project Conclusion](#12-project-conclusion)
* [13. Tools & Technologies Used](#13-tools--technologies-used)


---

## 1. Project Overview & Inspiration
This capstone project focuses on a brand with deep personal and cultural significance to me and the Washington, D.C. area. Born and raised in D.C., I selected Solbiato Sport because it represents a legendary landmark for our local fashion, music, and regional culture since 1979. In this project, I apply a data analytics framework to a piece of my hometown history, evaluating how the brand successfully pivoted its business model through an analytical lens.

## 2. The Georgetown Storefront History
For over forty years, Solbiato Sport operated as an exclusive boutique on Wisconsin Avenue, located in the prestigious neighborhood of Georgetown in Washington, D.C. Known for its multi-million dollar homes, high-end restaurants, and heavy pedestrian foot traffic, Georgetown provided an environment built on single-storefront demand and interactive, high-end customer service. However, as shopping habits across D.C. shifted during the 2020 pandemic era, traditional foot traffic was no longer a sustainable business pillar. My project evaluates the specific challenges they faced while trying to transition its luxury boutique energy into a scalable online consumer model.

## 3. Business Research Question
I wanted to answer one main question in this project: *How did a small, independent shop like Solbiato Sport survive the massive economic shifts in Georgetown that forced major corporate retail brands to close down completely?* 

To eliminate speculation, I anchored my research model directly into data across four key analytical lenses:
1. Online search trend patterns (Consumer digital intent)
2. Commercial real estate shifts within the Georgetown corridor
3. Internal website e-commerce inventory database code structures
4. Pricing bracket implementation strategies

## 4. Digital Search Volatility Analysis
Online search interest is a direct measure of how people discover an e-commerce brand. I tracked Google Trends data from 2004 to 2026 to see the big picture. The data shows strong momentum through the late 2000s when local consumers actively searched for this exclusive streetwear. However, heading into 2020, public search volume entered a severe downward trend. This proved that their regular online search presence was hitting a strong decline.

## 5. Annual Search Volatility Breakdown
I looked closely at the annual search trends to map out the exact decline in consumer intent. Between 2009 and 2011, Solbiato's search volume scores peaked at a maximum of 843 points. By 2020, this number plunged to 471, and ultimately hit an astonishing low of 74 points by 2026. This data showed me that relying on casual public searches online was no longer a working business model. The findings highlight a shift in digital strategy to get maximum value from dedicated, core online buyers.

## 6. Retail Challenges in Georgetown
The decline in digital discovery happened at the exact same time as major economic shifts in Solbiato's physical operating market. The brand's storefront sat right on the high-traffic commercial corridor of M Street and Wisconsin Avenue Northwest. While being on Wisconsin Avenue is usually a huge asset for retail foot traffic, rising financial burdens turned the local real estate market into a hostile environment for independent boutiques.

## 7. Commercial Real Estate Trends
I paired geographic mapping with official market data from the Georgetown Business Improvement District. This analysis revealed extreme economic risks in the local retail market that directly impacted brick-and-mortar survival:

* **Skyrocketing Vacancies:** Storefront vacancy in the district surged from a stable 5% baseline up to an astounding 14%.
* **Storefront Closures:** This vacancy spike represented 63 permanent storefront closures along the immediate corridor.
* **Premium Rental Costs:** Despite the high volume of empty spaces, landlords maintained commercial rents at a crushing premium averaging $145 to $175 per square foot.

These market pressures triggered the collapse of national retail giants like Brooks Brothers. The data proves that maintaining a physical storefront on Wisconsin Avenue was a financially unsustainable struggle, validating Solbiato's strategic decision to close their storefront, shift to an appointment-only showroom model, and reallocate their capital entirely into their online platform.

## 8. The Product Catalog Dashboard
To analyze Solbiato's shift to a 100% online business model, I designed a product catalog dashboard using Tableau. This dashboard tracks their active digital inventory metrics:

* **Total Catalog Volume:** 761 unique active products.
* **Total Catalog Value:** Over $47,000 in catalog value.
* **Strategic Catalog Shift:** A 100% focus on internal brand labels instead of third-party apparel.
* **Targeted Expansion:** A children's apparel collection locking in 211 active kids' styles. 

The website inventory structure leverages the brand's loyal adult buyer base by mirroring adult designs into youth sizes. This allows the business to convert single adult transactions into high-value, multi-generational family bundle orders.

## 9. The Three-Step Business Strategy
My analysis shows that Solbiato used a three-step strategy to successfully pivot their business and survive the retail crisis:

1. **Price Balancing:** Maintaining a balanced inventory mix that hits different consumer spending brackets.
2. **Brand Identity:** Preserving authentic local D.C. product names within their e-commerce store to protect established community loyalty.
3. **Cost Reduction:** Closing the physical storefront to eliminate premium rent costs and reallocating resources into digital infrastructure.

## 10. Website Inventory Data & Code Structure
When I audited the website inventory records, I found an intentional strategy to sell matching items across categories. The data shows line-for-line matching styles between the youth and adult categories using a parallel naming setup. Premium adult lines like `BAY BRIDGe`, `CAMPING`, and `REFLECTION` directly match youth items that start with a `K-` label (`K-BAY BRIDGE`, `K-CAMPING`, `K-REFLECTION`). This setup naturally cross-sells matching outfits on the website, turning single orders into full family packages while local competitors were struggling to survive.

## 11. Price Brackets & Profit Margins
My final pricing analysis shows how their price choices balance out to keep the online business thriving. The website sets an accessible, lower average price of $46.58 for youth items to encourage easy entry-level purchases. Meanwhile, the premium adult apparel lines hold strong at a highly profitable average price tier of $79.05. This strategy allows them to clear high inventory volumes with affordable kids items while holding premium prices on adult gear to protect their profit margins.

## 12. Project Conclusion
Solbiato Sport survived the Georgetown retail collapse by completely adapting how they run their business. By responding to declining public search trends, escaping high rent costs, using matching product names, and setting protective price tiers, the company protected its financial health. This project proves that a single independent streetwear business can use data and smart strategies to successfully navigate severe commercial real estate challenges and thrive online.

## 13. Tools & Technologies Used
Since there was no ready-made dataset available online, I built this entire data project from scratch using the following tools:

* **Web Scraping:** I wrote a custom Python script in VS Code using the BeautifulSoup library to collect live product data straight from their website.
* **Data Cleaning:** I used the Python Pandas library to clean up the raw file, fix pricing text columns, and organize the data so it can be easily read without errors.
* **Data Visualization:** I designed interactive dashboards and charts using Tableau Desktop to easily analyze and display pricing trends and catalog volume.
