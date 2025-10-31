# 🧠 Project Overview — نظرة عامة على المشروع — Aperçu du projet

This project aims to **annotate X-ray images from El Oued hospitals (local dataset)** in order to build an **AI model capable of detecting, localizing, and describing bone fractures**.  
The annotated data will serve as a foundation for developing a **computer vision system** that assists doctors in **automated diagnosis and structured reporting** of fractures.  

---

<div dir="rtl">

يهدف هذا المشروع إلى **وصف (Annotation) صور الأشعة المأخوذة من مستشفيات الوادي** لبناء **نظام ذكاء اصطناعي قادر على تحديد موقع الكسر ووصف خصائصه الطبية بدقة**.  
سيتم استخدام البيانات المعلّمة لتدريب نموذج رؤية حاسوبية يساعد الأطباء في **تشخيص الكسور وإعداد تقارير طبية تلقائية**.

</div>

---

Ce projet a pour but **d’annoter les radiographies provenant des hôpitaux d’El Oued** afin de développer un **modèle d’IA capable de détecter, localiser et décrire les fractures osseuses**.  
Les annotations serviront à entraîner un système de **vision par ordinateur** qui assistera les médecins dans le **diagnostic automatique et la génération de rapports médicaux structurés**.

---

# 🦴 Fracture Annotation Template — نموذج توصيف الكسر — Modèle d’annotation de fracture

## 1. Fracture Characteristics — خصائص الكسر — Caractéristiques de la fracture

| الحقل | English | Français | <div dir="rtl">الشرح العربي</div> |
|--------|----------|-----------|----------------------------------|
| اسم العظم | Bone name | Nom de l’os | <div dir="rtl">اسم العظم الذي حدث فيه الكسر (مثل: الكعبرة، الزند، الفخذ...)</div> |
| موقع الكسر | Proximal / Middle / Distal third | Tiers proximal / moyen / distal | <div dir="rtl">موقع الكسر على طول العظم</div> |
| نوع الكسر | Simple (Two-part) / Transverse / Oblique / Spiral / Complex / Comminuted / Butterfly | Simple (En deux parties) / Transversale / Oblique / Spirale / Complexe / Comminutive / En aile de papillon | <div dir="rtl">نوع الكسر وشكله</div> |
| الإزاحة | Non-displaced / Displaced (mm or degrees) | Non déplacée / Déplacée (mm ou degrés) | <div dir="rtl">هل تحركت أجزاء العظم عن موضعها الطبيعي</div> |
| الزاوية | Approximate angle between fragments | Angle approximatif entre les fragments | <div dir="rtl">الزاوية التقريبية بين القطع المكسورة</div> |
| الدوران | Yes / No (if visible) | Oui / Non (si visible) | <div dir="rtl">هل يوجد دوران واضح في اتجاه العظم</div> |
| عدد القطع | Number of bone fragments | Nombre de fragments osseux | <div dir="rtl">عدد القطع العظمية المرئية في الصورة</div> |
| الأنسجة الرخوة | Yes / No | Oui / Non | <div dir="rtl">هل توجد إصابة في الأنسجة الرخوة المحيطة</div> |
| فقدان النسيج العظمي | Present / Absent | Présente / Absente | <div dir="rtl">وجود نقص في النسيج العظمي</div> |
| تمزق القشرة | Present / Absent | Présente / Absente | <div dir="rtl">تمزق في الطبقة الخارجية الصلبة للعظم</div> |
| أمراض عظمية | Osteoporosis / Primary tumor / Metastasis / Tuberculosis | Ostéoporose / Tumeur primaire / Métastase / Tuberculose | <div dir="rtl">أمراض عظمية مرافقة محتملة</div> |
| الفئة العمرية | Child / Adult / Elderly | Enfant / Adulte / Âgé | <div dir="rtl">الفئة العمرية للمريض</div> |

---

## 2. Fracture Localization — توطين بؤرة الكسر — Localisation de la fracture

| الحقل | English | Français | <div dir="rtl">الشرح العربي</div> |
|--------|----------|-----------|----------------------------------|
| جسم العظم | Diaphyseal region | Région diaphysaire | <div dir="rtl">في جسم العظم (الجزء الأوسط)</div> |
| المنطقة الميتافيسية | Metaphyseal region | Région métaphysaire | <div dir="rtl">في المنطقة بين الجسم والمفصل</div> |
| المشاش-الميتافيس | Epiphyso-metaphyseal region | Région épiphyso-métaphysaire | <div dir="rtl">يشمل المشاش والميتافيس</div> |
| الانفصال / الخلع | Disarticulation / Dislocation | Désarticulation / Luxation | <div dir="rtl">انفصال أو خلع في المفصل أو الأسطح العظمية</div> |

---

## 3. Bone Pathologies — الأمراض العظمية — Pathologies osseuses

| الحقل | English | Français | <div dir="rtl">الشرح العربي</div> |
|--------|----------|-----------|----------------------------------|
| ورم عظمي أولي | Primary bone tumor | Néoplasie osseuse primaire | <div dir="rtl">ورم عظمي ينشأ داخل العظم</div> |
| ورم عظمي ثانوي | Secondary bone tumor | Lésion osseuse métastatique | <div dir="rtl">ورم عظمي ناتج عن انتشار سرطان من عضو آخر</div> |
| هشاشة العظام | Osteoporosis | Ostéoporose | <div dir="rtl">ضعف وهشاشة في العظم تقلل كثافته</div> |
| سلّ العظام | Bone tuberculosis | Tuberculose osseuse | <div dir="rtl">عدوى عظمية ناتجة عن بكتيريا السل</div> |

---

## 4. Treatment — العلاج — Traitement

| الحقل | English | Français | <div dir="rtl">الشرح العربي</div> |
|--------|----------|-----------|----------------------------------|
| العلاج غير الجراحي | Orthopedic / Cast / Splint / Circular cast | Orthopédique / Plâtre / Atelle / Circulaire | <div dir="rtl">علاج غير جراحي مثل الجبيرة أو التجبير</div> |
| العلاج الجراحي | Reduction and fixation (plates, screws, rods, etc.) | Réduction et fixation (plaques, vis, tiges, etc.) | <div dir="rtl">علاج جراحي يتضمن رد الكسر وتثبيته بأدوات معدنية</div> |

---

## 5. Image Metadata — بيانات الصورة — Métadonnées de l’image

| الحقل | English | Français | <div dir="rtl">الشرح العربي</div> |
|--------|----------|-----------|----------------------------------|
| نوع التصوير | AP / Lateral / Oblique | AP / Latérale / Oblique | <div dir="rtl">نوع أو زاوية التصوير بالأشعة</div> |
| الجزء المصور | Forearm / Leg / Hand / etc. | Avant-bras / Jambe / Main / etc. | <div dir="rtl">الجزء المصوَّر من الجسم</div> |
| الجهة | Left / Right | Gauche / Droite | <div dir="rtl">الجهة المصوَّرة (يسار أو يمين)</div> |
| الفئة العمرية | Child / Adult / Elderly | Enfant / Adulte / Âgé | <div dir="rtl">الفئة العمرية للمريض</div> |
| آلية الإصابة | Fall / Accident / Sports injury | Chute / Accident / Blessure sportive | <div dir="rtl">آلية أو سبب الإصابة إن كانت معروفة</div> |
