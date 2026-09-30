# 📚 คลังศัพท์ ITDS231 (Lecture 1–7)

> รวมศัพท์จากสไลด์ทุก Lecture (L1–2, L3–4, L5.0, L5.1, L5.2, L6.1, L6.2, L7) อธิบายสั้นๆ พอเข้าใจ ใช้ทวนก่อนสอบ
> ศัพท์ที่มีเครื่องหมาย 📎 คือไม่อยู่ในข้อความสไลด์ (สไลด์เป็นรูป) เขียนจากความรู้พื้นฐานตาม syllabus ให้เช็กกับสไลด์อีกที
> กดที่นี่ดูหน้าเว็ปที่นี่ >> https://thinnaphat-tht.github.io/itds231-glossary/

## สารบัญ

- [Lecture 1–2 — Introduction to Computer Networks](#-lecture-12--introduction-to-computer-networks)
- [Lecture 3–4 — Application Layer, HTTP, Email, DNS, Video/CDN](#-lecture-34--application-layer-http-email-dns-videocdn)
- [Lecture 5.0 — Data Link Layer Foundation](#-lecture-50--data-link-layer-foundation)
- [Lecture 5.1 — Error Detection & Correction](#-lecture-51--error-detection--correction)
- [Lecture 5.2 — Flow Control, ARQ, HDLC](#-lecture-52--flow-control-arq-hdlc)
- [Lecture 6.1 — Media Access Control (MAC)](#-lecture-61--media-access-control-mac)
- [Lecture 6.2 — Ethernet](#-lecture-62--ethernet)
- [Lecture 7 — ARP, Switch, STP, VLAN](#-lecture-7--arp-switch-stp-vlan)
- [Quiz คำศัพท์](#quiz-คำศัพท์)

## 🌐 Lecture 1–2 — Introduction to Computer Networks

| ศัพท์ | คืออะไร |
|---|---|
| **Internet** | เครือข่ายของเครือข่าย (network of networks) ที่ ISP ต่างๆ เชื่อมต่อกัน |
| **Host / End system** | อุปกรณ์ปลายทางที่รันแอป เช่น PC มือถือ server อยู่ที่ขอบ (edge) ของ Internet |
| **Packet switch** | อุปกรณ์ที่ส่งต่อ packet เช่น router และ switch |
| **ISP** | Internet Service Provider ผู้ให้บริการอินเทอร์เน็ต |
| **Tier-1 ISP** | ISP ใหญ่ระดับแกนกลาง ครอบคลุมระดับชาติและนานาชาติ เช่น AT&T, NTT |
| **IXP** | Internet Exchange Point จุดที่ ISP หลายเจ้ามาเชื่อมกัน (peering link) |
| **Content provider network** | เครือข่ายส่วนตัวของ Google, Facebook ที่ต่อ data center ตรงไปหาผู้ใช้ โดยไม่ผ่าน ISP ใหญ่ |
| **Protocol** | กติกาที่กำหนดรูปแบบและลำดับของข้อความ รวมถึงการกระทำเมื่อส่ง/รับข้อความ เช่น HTTP, TCP, IP |
| **RFC / IETF** | RFC = Request for Comments เอกสารมาตรฐาน Internet · IETF = องค์กรที่ออกมาตรฐาน |
| **Network edge** | ส่วนขอบ: host (client/server) และ access network |
| **Access network** | เครือข่ายที่ต่อ end system เข้ากับ edge router เช่น cable, DSL, WiFi, 4G/5G, Ethernet |
| **Network core** | ส่วนแกนกลาง: mesh ของ router ที่เชื่อมกัน |
| **HFC** | Hybrid Fiber Coax เคเบิลทีวี/อินเทอร์เน็ตผ่านสาย coax+fiber แบบ asymmetric (ขาลงเร็วกว่าขาขึ้น) และบ้านแชร์สายกัน |
| **CMTS / Cable modem** | อุปกรณ์ที่ปลายสาย cable ฝั่ง ISP (CMTS) และฝั่งบ้าน (modem) |
| **FDM** | Frequency Division Multiplexing แบ่งช่องสัญญาณตามย่านความถี่ |
| **DSL / DSLAM** | ใช้สายโทรศัพท์เดิม ส่ง voice กับ data คนละความถี่ไปที่ DSLAM ของ central office แบบ dedicated line |
| **WLAN / WiFi** | เครือข่ายไร้สายในพื้นที่ใกล้ (มาตรฐาน 802.11) ผ่าน access point |
| **Twisted pair / Coaxial / Fiber optic** | สื่อนำสัญญาณแบบมีสาย: สายทองแดงเกลียวคู่ (Cat5, Cat6) · สาย coax หุ้มซ้อนแกนร่วม · ใยแก้วส่งแสง เร็วสุดและทนสัญญาณรบกวน |
| **Guided / Unguided media** | Guided = สัญญาณวิ่งในสายจริง · Unguided = สัญญาณวิ่งในอากาศ เช่น radio |
| **Bandwidth / Link capacity (R)** | อัตราส่งข้อมูลของลิงก์ หน่วย bps |
| **Packet** | ก้อนข้อมูลที่ host หั่นจากข้อความแอป ขนาด L บิต |
| **Packet switching** | หั่นข้อมูลเป็น packet แชร์ลิงก์กัน เหมาะกับข้อมูลเป็นช่วงๆ (bursty) แต่อาจคิวยาวหรือ packet หาย |
| **Circuit switching** | จองช่องสัญญาณตลอดการโทร (dedicated) ประสิทธิภาพคงที่ แต่ช่องว่างแล้วไม่มีใครใช้ได้ ใช้ในโทรศัพท์แบบเดิม |
| **TDM** | Time Division Multiplexing แบ่งตามช่วงเวลา (time slot) |
| **Store-and-forward** | router ต้องได้รับ packet ครบทั้งก้อนก่อน จึงส่งต่อไปลิงก์ถัดไปได้ |
| **Forwarding** | การกระทำภายใน router: ย้าย packet จาก input link ไป output link ตาม forwarding table (local) |
| **Routing** | การหาเส้นทางจากต้นทางถึงปลายทางด้วย routing algorithm (global) |
| **Transmission delay** | เวลาผลัก packet ลงสาย = L/R |
| **Propagation delay** | เวลาสัญญาณเดินทางบนสาย = d/s (d = ความยาวสาย, s = ความเร็วสัญญาณ ราว 2x10^8 m/s) |
| **Processing delay** | เวลาที่ router ตรวจ bit error และเลือก output link (เล็กมาก) |
| **Queueing delay** | เวลารอคิวที่ output link ขึ้นกับความหนาแน่นของ traffic |
| **Nodal delay** | รวม 4 delay = proc + queue + trans + prop |
| **Traffic intensity** | La/R (a = อัตรา packet เข้า) ถ้าเข้าใกล้ 1 คิวยาวมาก ถ้าเกิน 1 delay เป็นอนันต์ |
| **Packet loss** | packet ที่มาตอนบัฟเฟอร์เต็มจะถูกทิ้ง |
| **Throughput** | อัตราบิตที่ส่งถึงผู้รับจริง (bits ต่อหน่วยเวลา) |
| **Bottleneck link** | ลิงก์ที่ช้าสุดบนเส้นทาง เป็นตัวจำกัด throughput ปลายทาง |
| **RTT** | Round-Trip Time เวลาที่ packet เล็กไปกลับระหว่าง client กับ server |
| **traceroute** | โปรแกรมวัด delay ไปยัง router แต่ละตัวบนเส้นทาง โดยใช้ TTL |
| **Layering / Protocol stack** | แบ่งระบบเป็นชั้น แต่ละชั้นให้บริการชั้นบน Internet มี 5 ชั้น: application, transport, network, link, physical |
| **OSI model** | โมเดล 7 ชั้น เพิ่ม presentation (เข้ารหัส/บีบอัด) และ session (ซิงก์/ฟื้นข้อมูล) ซึ่ง Internet ไม่มี |
| **Encapsulation** | แต่ละชั้นห่อข้อมูลด้วย header ของตัวเอง: message → segment → datagram → frame |
| **Segment / Datagram / Frame** | หน่วยข้อมูลของ transport / network / link layer ตามลำดับ |
| **Packet sniffing** | ดักอ่าน packet ที่ผ่านสื่อแชร์ (เช่น WiFi) ตัวอย่างโปรแกรม Wireshark |
| **IP spoofing** | ส่ง packet ที่ปลอม IP ต้นทางเพื่อหลอกปลายทาง |
| **DoS / DDoS** | ถล่มเป้าหมายด้วย traffic ปลอมจนใช้งานไม่ได้ DoS มาจากแหล่งเดียว DDoS มาจากหลายเครื่อง (botnet) |
| **Botnet** | เครือข่ายเครื่องที่ถูกฝังมัลแวร์ ใช้เป็นฐานโจมตี DDoS |
| **Firewall** | middlebox กรอง packet ที่เข้าออก ตั้งค่าเริ่มต้นแบบปิดทุกอย่างไว้ก่อน |
| **Authentication / Confidentiality / Integrity** | พิสูจน์ตัวตน / ปิดลับด้วยการเข้ารหัส / ตรวจว่าข้อมูลไม่ถูกแก้ (digital signature) |
| **ARPAnet** | เครือข่าย packet-switching ตัวแรก (1969) ต้นกำเนิด Internet |
| **ALOHAnet** | เครือข่ายดาวเทียมที่ฮาวาย (1970) ต้นแบบของ random access และ Ethernet |
| 📎 **Topology** | รูปแบบการเชื่อมต่อ: bus (สายเส้นเดียว), star (ต่อที่ศูนย์กลาง), ring (วงแหวน), mesh (ต่อกันหลายทาง) · physical = การเดินสายจริง, logical = การเชื่อมตาม IP/interface |
| 📎 **Nyquist / Shannon** | สูตร data rate limit: Nyquist = ช่องไร้ noise, Shannon = ช่องมี noise (ขึ้นกับ bandwidth และ SNR) |

---

## 🖥️ Lecture 3–4 — Application Layer, HTTP, Email, DNS, Video/CDN

| ศัพท์ | คืออะไร |
|---|---|
| **Application layer** | ชั้นบนสุด ที่แอปคุยกันผ่าน protocol เช่น HTTP, SMTP, DNS แอปรันที่ end system เท่านั้น ไม่รันใน router |
| **Client-Server** | server เปิดตลอด มี IP ถาวร client ติดต่อ server และไม่คุยกันเอง เช่น HTTP, IMAP, FTP |
| **P2P (Peer-to-Peer)** | ไม่มี server กลาง ทุกเครื่องเป็นทั้งผู้ขอและผู้ให้บริการ ยิ่งคนเยอะยิ่งเร็ว เช่น BitTorrent, blockchain |
| **Process** | โปรแกรมที่รันอยู่ในเครื่อง ในเครื่องเดียวกันคุยกันด้วย IPC ข้ามเครื่องคุยด้วยการส่ง message |
| **IPC** | Inter-Process Communication การสื่อสารระหว่าง process ในเครื่องเดียวกัน (OS จัดการ) |
| **Client process / Server process** | ฝ่ายเริ่มติดต่อ / ฝ่ายรอให้ติดต่อ |
| **Socket** | ประตูระหว่างแอปกับ transport layer process ส่ง/รับ message ผ่าน socket |
| **IP address + Port number** | ใช้ระบุ process ข้ามเครือข่าย IP บอกเครื่อง port บอกว่าเป็นแอปไหนในเครื่อง |
| **PID** | Process ID เลขประจำ process ภายในเครื่อง |
| **TCP** | ส่งแบบเชื่อถือได้ (reliable) มี flow control, congestion control ต้อง setup connection แต่ไม่รับประกันเวลา/ความเร็ว/ความปลอดภัย |
| **UDP** | ส่งแบบไม่รับประกัน ไม่มี connection, flow control, congestion control ข้อมูลอาจหายหรือสลับลำดับ แต่เบาและเร็ว |
| **TLS** | Transport Layer Security เข้ารหัส TCP connection พร้อมตรวจ integrity และ authentication ทำงานในชั้น application |
| **Web object / URL** | หน้าเว็บประกอบด้วย object (HTML, รูป, CSS, JS) แต่ละชิ้นมี URL = host name + path name |
| **Base HTML file** | ไฟล์ HTML หลักที่อ้างถึง object อื่นๆ ในหน้า |
| **HTTP** | HyperText Transfer Protocol โปรโตคอลของเว็บ แบบ client/server ใช้ TCP port 80 |
| **Stateless** | server ไม่จำประวัติ request ก่อนหน้าของ client (เพราะ state ซับซ้อน ถ้า crash ข้อมูลไม่ตรงกัน) |
| **Non-persistent HTTP** | 1 TCP connection ส่งได้ 1 object เสร็จแล้วปิด เวลาตอบ = 2 RTT + เวลาส่งไฟล์ต่อ object |
| **Persistent HTTP (HTTP/1.1)** | เปิด connection ไว้ ส่งหลาย object ผ่านสายเดียว ลดเหลือราว 1 RTT สำหรับ object ที่เหลือ |
| **HTTP request message** | ข้อความ ASCII ประกอบด้วย request line (GET/POST/HEAD), header lines และ body |
| **GET / POST / HEAD / PUT** | GET ขอ object · POST ส่งข้อมูลฟอร์มใน body · HEAD ขอเฉพาะ header · PUT อัปโหลดไฟล์ทับของเดิม |
| **HTTP response / Status code** | ข้อความตอบกลับ มี status line เช่น 200 OK (สำเร็จ), 304 Not Modified, 404 Not Found |
| **Cookie** | ตัวช่วยให้ server จำ user มี 4 ส่วน: Set-Cookie ใน response, ไฟล์ cookie ที่ browser, Cookie header ใน request, ฐานข้อมูลหลังบ้าน ใช้ทำ session, ตะกร้า, tracking |
| **First-party / Third-party cookie** | First-party มาจากเว็บที่เราเข้า · Third-party มาจากบริษัทโฆษณาที่ฝังโค้ดในเว็บ ใช้ตาม user ข้ามเว็บ (targeted ads) Firefox และ Safari บล็อกเป็นค่าเริ่มต้น |
| **GDPR** | กฎหมายคุ้มครองข้อมูลส่วนบุคคลของ EU ถือว่า cookie ที่ระบุตัวบุคคลได้เป็นข้อมูลส่วนบุคคล |
| **Web cache / Proxy server** | ที่เก็บสำเนา object ใกล้ client ตอบแทน origin server ได้ (เป็นทั้ง client และ server) ลด response time และ traffic ที่ access link |
| **Forward proxy / Reverse proxy** | Forward อยู่ฝั่ง client (ซ่อน IP, กรองเว็บ, cache ในองค์กร) · Reverse อยู่ฝั่ง server (load balancing, ป้องกัน, cache ไฟล์คงที่) |
| **Cache hit / miss** | hit = มีใน cache ตอบเลย · miss = ไม่มี ต้องไปขอ origin server Average delay = hit rate x delay hit + miss rate x delay miss |
| **Cache-Control** | header บอกว่าแคชได้นานเท่าไร เช่น max-age=3600 (1 ชั่วโมง) หรือ no-cache (ต้องถาม server ทุกครั้ง) |
| **Conditional GET** | ส่ง If-modified-since ไป ถ้าไฟล์ไม่เปลี่ยน server ตอบ 304 Not Modified (ไม่ส่งไฟล์) ถ้าเปลี่ยนตอบ 200 OK พร้อมไฟล์ใหม่ |
| **HTTP/2** | แบ่ง object เป็น frame แล้วส่งสลับกัน (multiplexing) ตั้ง priority ได้ และ server push ได้ เพื่อลด HOL blocking |
| **HOL blocking** | Head-of-Line blocking object เล็กต้องรอหลัง object ใหญ่ที่มาก่อน (FCFS) ใน HTTP/1.1 และถ้า TCP packet หายทุก object หยุดรอ |
| **QUIC / HTTP/3** | QUIC = protocol ระดับ application บน UDP รวม handshake เหลือ 1 RTT (บางกรณี 0-RTT) มี error/congestion control เอง HTTP/3 ทำงานบน QUIC |
| **Port ที่ควรจำ** | 80 HTTP · 443 HTTPS · 25 SMTP · 53 DNS · 21/20 FTP · 22 SSH · 110 POP3 · 143 IMAP |
| **User agent** | โปรแกรมอ่าน/เขียนอีเมล เช่น Outlook |
| **Mail server** | เก็บกล่องจดหมาย (mailbox) และคิวข้อความขาออก |
| **SMTP** | Simple Mail Transfer Protocol ส่งอีเมลระหว่าง mail server ใช้ TCP port 25 มี 3 ช่วง: handshake, transfer, closure |
| **IMAP / POP3** | mail access protocol ใช้ดึงอีเมลจาก server มาอ่าน (SMTP ใช้ส่ง ไม่ใช่ดึง) IMAP เก็บบน server และจัดโฟลเดอร์ได้ |
| **DNS** | Domain Name System ฐานข้อมูลแบบกระจายเป็นลำดับชั้น แปลงชื่อเป็น IP address และให้บริการอื่นเช่น alias, mail server name, load distribution |
| **Root / TLD / Authoritative server** | Root (ที่พึ่งสุดท้าย 13 ชุด ICANN ดูแล) → TLD (.com .org .edu .th) → Authoritative (ของแต่ละองค์กร ให้ชื่อเป็น IP จริง) |
| **Local DNS server** | DNS ที่ host ถามก่อน (ของ ISP) ตอบจาก cache หรือส่งต่อเข้าลำดับชั้น |
| **Iterated / Recursive query** | Iterated = server ตอบว่าไปถามใครต่อ · Recursive = โยนภาระหาคำตอบให้ server ที่ถูกถาม |
| **DNS caching / TTL** | จำผลแปลงชื่อไว้ชั่วคราว หมดอายุตาม TTL ทำให้เร็วแต่อาจล้าสมัย |
| **Resource Record (RR)** | รายการใน DNS รูปแบบ (name, value, type, ttl) ชนิด: A (ชื่อ → IP), NS (โดเมน → ชื่อ authoritative server), CNAME (ชื่อเล่น → ชื่อจริง), MX (ชื่อ mail server) |
| **DNSSEC / DNS cache poisoning** | DNSSEC = การยืนยันตัวตนให้ DNS · Cache poisoning = หลอก DNS ให้จำ IP ปลอม |
| **Spatial / Temporal coding** | บีบวิดีโอโดยใช้ความซ้ำภายในภาพ / ส่งเฉพาะส่วนต่างจากเฟรมก่อน |
| **CBR / VBR** | Constant / Variable Bit Rate อัตราการเข้ารหัสวิดีโอคงที่ / เปลี่ยนตามเนื้อหา |
| **Jitter / Playout buffer** | Jitter = delay เครือข่ายไม่คงที่ · Playout buffer = บัฟเฟอร์ฝั่ง client หน่วงการเล่นเพื่อให้เล่นต่อเนื่อง |
| **DASH** | Dynamic Adaptive Streaming over HTTP แบ่งวิดีโอเป็น chunk หลายคุณภาพ client เลือกเองตามแบนด์วิดท์ที่วัดได้ อ่านจาก manifest file |
| **Manifest file** | ไฟล์รายการ URL ของ chunk แต่ละคุณภาพ |
| **CDN** | Content Delivery Network กระจายสำเนาวิดีโอ/เนื้อหาไปไว้ server ใกล้ผู้ใช้ แก้ปัญหา mega-server เดียวที่ไม่ scale (เช่น Akamai, Netflix Open Connect) |
| **OTT** | Over-The-Top บริการส่งเนื้อหาบน Internet โดยไม่ผ่านผู้ให้บริการเครือข่ายโดยตรง เช่น Netflix |
| **Socket programming UDP vs TCP** | UDP = ไม่มี connection ต้องแนบ IP+port ปลายทางทุก packet · TCP = ต้อง handshake ก่อน เป็น byte stream ที่เชื่อถือได้ |

---

## 🔗 Lecture 5.0 — Data Link Layer Foundation

| ศัพท์ | คืออะไร |
|---|---|
| **Data Link Layer (DLL)** | ชั้นที่จัดการส่งข้อมูลข้ามลิงก์เดียว (hop เดียว) ต่างจาก physical ที่ส่งแค่บิต |
| **Frame** | หน่วยข้อมูลของ DLL ห่อ packet ด้วย header และ trailer |
| **Hop-by-hop delivery** | DLL ส่งทีละช่วงลิงก์ ทุก router จะแกะ frame เก่าแล้วสร้าง frame ใหม่สำหรับลิงก์ถัดไป |
| **Framing** | แบ่งสตรีมบิตเป็น frame โดยกำหนดขอบเขตให้ผู้รับแยกแต่ละ frame ออก |
| **FCS** | Frame Check Sequence ค่าตรวจ error ท้าย frame (trailer) ส่วนใหญ่คำนวณแบบ CRC |
| **Header / Payload / Trailer** | ส่วนหัว (ที่อยู่ ควบคุม) / ข้อมูลจาก network layer / ส่วนท้าย (FCS) |
| **LLC** | Logical Link Control ซับเลเยอร์บน เชื่อมกับ network layer และ multiplex protocol ชั้นบน |
| **MAC (sublayer)** | Media Access Control ซับเลเยอร์ล่าง ทำ framing, link addressing, FCS และการแย่งใช้สื่อที่แชร์ |
| **Dedicated link / Shared link** | Dedicated = ลิงก์เฉพาะคู่ (full-duplex switch) · Shared = หลายเครื่องแชร์สื่อเดียว (bus, WiFi) ต้องมีกติกาแย่งใช้ |
| **Multiple access** | ปัญหาที่หลายเครื่องแชร์ช่องเดียวแล้วอาจส่งพร้อมกัน จึงต้องมี MAC protocol |
| **Byte-oriented framing** | frame ประกอบจากตัวอักษร 8 บิต ใช้ byte ตัวพิเศษเป็นตัวแบ่ง (เช่น PPP) |
| **Bit-oriented framing** | frame เป็นสตรีมบิตล้วน ใช้ flag pattern เป็นตัวแบ่ง (เช่น HDLC) |
| **Byte stuffing** | ถ้า flag byte โผล่ในข้อมูล ให้แทรก ESC (escape character) นำหน้า ผู้รับจะไม่เข้าใจผิดว่าเป็นตัวแบ่ง frame |
| **Bit stuffing** | ถ้าเจอบิต 1 ติดกัน 5 ตัวในข้อมูล ให้แทรก 0 ทันที เพื่อไม่ให้เหมือน flag 01111110 (0x7E) ของ HDLC |
| **Flag** | รูปแบบบิต/ไบต์พิเศษที่ใช้ทำเครื่องหมายต้นและท้าย frame (HDLC = 01111110) |
| **Length / Fixed-size framing** | บอกขอบเขตด้วยฟิลด์ความยาวหรือขนาดคงที่ ไม่ต้อง stuffing (เช่น Ethernet, 802.11) Ethernet padding ไม่ใช่ stuffing |
| **PPP** | Point-to-Point Protocol โปรโตคอลแบบจุดต่อจุด ทำ framing เอง ใช้ใน PPPoE ของ broadband/DSL |
| **HDLC** | High-Level Data Link Control โปรโตคอล DLL แบบ bit-oriented ใช้ใน WAN serial link |

---

## 🛡️ Lecture 5.1 — Error Detection & Correction

| ศัพท์ | คืออะไร |
|---|---|
| **Noise** | สัญญาณรบกวนที่ทำให้บิตเพี้ยน เช่น thermal noise, สัญญาณแทรก, ฟ้าผ่า |
| **Single-bit error** | ผิดเพียง 1 บิต |
| **Burst error** | ผิดหลายบิตติดกันเป็นช่วง ของจริงบนสายส่วนใหญ่เป็นแบบนี้ |
| **Redundancy** | บิตซ้ำซ้อนที่แนบไปกับข้อมูลเพื่อให้ผู้รับตรวจเองได้ แล้วทิ้งหลังตรวจเสร็จ |
| **Block coding** | หั่นข้อมูลเป็นบล็อก แนบบิตตรวจสอบต่อบล็อก |
| **Dataword / Codeword** | Dataword = ข้อมูลเดิม k บิต · Codeword = ข้อมูล+redundancy รวม n บิต โดย n = k + r |
| **ARQ** | Automatic Repeat reQuest ตรวจพบ error แล้วขอส่งใหม่ |
| **FEC** | Forward Error Correction แนบ redundancy มากพอให้ผู้รับซ่อมเองโดยไม่ต้องส่งใหม่ |
| **Parity check** | เติม 1 บิตให้จำนวนบิต 1 เป็นคู่ (even) หรือคี่ (odd) จับ error จำนวนคี่ได้ แต่จับจำนวนคู่ไม่ได้ |
| **Syndrome** | ค่าที่ผู้รับคำนวณจาก codeword ที่ได้รับ = 0 แปลว่าไม่มี error ≠ 0 แปลว่ามี error ใน Hamming syndrome คือตำแหน่งบิตที่ผิด |
| **2D parity** | ตรวจ parity ทั้งแถวและหลัก หาจุดตัดของแถวกับหลักที่ผิดได้ จึงแก้ได้ 1 บิต |
| **Checksum** | แบ่งข้อมูลเป็นชุด m บิต บวกแบบ one's complement (ตัวทดวนกลับมาบวก) แล้ว complement ส่งไปด้วย ผู้รับบวกรวมแล้วได้ 0 = ปกติ ใช้ใน IPv4 header, TCP, UDP |
| **One's complement** | การบวกที่เอาตัวทดล้นมาบวกกลับท้ายสุด แล้วกลับบิตผลลัพธ์ |
| **CRC** | Cyclic Redundancy Check หารด้วย divisor แบบ modulo-2 (XOR) ตกลงกันไว้ เศษที่ได้ (CRC) ต่อท้ายข้อมูล แม่นสุดสำหรับ burst error ใช้เป็น FCS ของ Ethernet |
| **Divisor / Generator** | ตัวหารที่ตกลงกันไว้ของ CRC CRC มีบิตน้อยกว่า divisor 1 บิตเสมอ |
| **Modulo-2 division** | การหารไบนารีที่ลบ = XOR (ไม่มีตัวยืม) |
| **Hamming code** | วาง parity bit ที่ตำแหน่งกำลังสอง (1, 2, 4, 8) แต่ละตัวคุมคนละกลุ่มบิต แก้ error ได้ 1 บิต อ่านตำแหน่งจาก (r8 r4 r2 r1) |
| **Interleaving** | สลับลำดับบิตระหว่างหลาย codeword ก่อนส่ง เพื่อให้ burst error กลายเป็น error 1 บิตต่อ codeword แล้วใช้ Hamming ซ่อมได้ |

---

## 🚦 Lecture 5.2 — Flow Control, ARQ, HDLC

| ศัพท์ | คืออะไร |
|---|---|
| **Flow control** | คุมอัตราส่งของ sender ไม่ให้ผู้รับรับไม่ทันจนบัฟเฟอร์ล้น |
| **Error control** | ตรวจจับ error และจัดการ (ส่งซ้ำ) เมื่อ frame เสียหายหรือหาย |
| **Buffer** | ที่พักข้อมูลชั่วคราว ฝั่ง sender เก็บ frame ที่รอส่ง/ส่งซ้ำ ฝั่ง receiver เก็บ frame ที่รอส่งต่อชั้นบน |
| **ACK / NAK** | ACK = ยืนยันรับ frame ถูกต้อง · NAK = แจ้งให้ส่ง frame นั้นใหม่ |
| **Timer / Timeout** | sender จับเวลารอ ACK ถ้าไม่มา ถือว่า frame หาย ต้องส่งซ้ำ |
| **Sequence number** | เลขกำกับ frame เพื่อแยก frame ใหม่กับ frame ซ้ำ ใช้ m บิต = เลข 0 ถึง 2^m − 1 แล้ววนกลับ |
| **Simple protocol** | ไม่มี flow control และ error control |
| **Stop-and-Wait ARQ** | ส่งทีละ 1 frame รอ ACK ก่อนส่งตัวต่อไป ใช้เลข 0 กับ 1 สลับกัน ง่ายแต่ช้า ไม่ใช้ประโยชน์ลิงก์เร็ว/หน่วงนาน |
| **S และ R (Stop-and-Wait)** | S = เลขของ frame ที่กำลังส่ง ฝั่ง sender · R = เลขของ frame ถัดไปที่ receiver รอรับ ACK n = frame ก่อน n ครบแล้ว รอ frame n |
| **Pipelining** | ส่งหลาย frame ต่อเนื่องโดยไม่ต้องรอ ACK ทีละตัว (GBN และ SR ใช้ · Stop-and-Wait ไม่ใช้) |
| **Sliding window** | หน้าต่างที่กำหนดจำนวน frame ที่ส่งค้างได้ เมื่อได้ ACK หน้าต่างเลื่อนไปข้างหน้า |
| **Sf / Sn / R (Sliding window)** | Sf = frame แรกสุดที่ส่งแล้วยังไม่ได้ ACK · Sn = frame ถัดไปที่จะส่ง · R (Rn) = frame ที่ receiver รอรับ |
| **Outstanding frame** | frame ที่ส่งไปแล้วแต่ยังไม่ได้ ACK sender ต้องเก็บสำเนาไว้ |
| **Go-Back-N ARQ** | ส่ง pipeline ได้ sender window ไม่เกิน 2^m − 1 receiver window = 1 รับเฉพาะ frame ที่รอ ตัวที่มาผิดลำดับทิ้ง ถ้า timeout ส่งซ้ำตั้งแต่ frame เก่าสุดที่ไม่ได้ ACK ไปทั้งหมด |
| **Cumulative ACK** | ACK n แปลว่า frame ก่อน n ครบทั้งหมดแล้ว และรอ frame n ใช้ใน GBN |
| **Selective Repeat ARQ** | รับ frame ผิดลำดับได้และเก็บ buffer ส่งซ้ำเฉพาะ frame ที่หายหรือเสีย window ของทั้งสองฝั่งไม่เกิน 2^(m−1) แต่ละ frame มี timer แยก |
| **Individual ACK** | ACK ทีละ frame ที่รับถูกต้อง ใช้ใน Selective Repeat |
| **Piggybacking** | ส่ง ACK ติดไปกับ data frame ที่วิ่งสวนทางกัน เพื่อประหยัด |
| **Bandwidth-delay product** | bandwidth x round-trip delay = จำนวนบิตที่ส่งได้ระหว่างรอ ACK ใช้วัดว่า window ควรใหญ่เท่าไร |
| **Link utilization** | ส่งจริงหารด้วย bandwidth-delay product Stop-and-Wait ต่ำมาก (เช่น 5%) GBN สูงกว่าตามขนาด window |
| **HDLC** | โปรโตคอล bit-oriented มาตรฐาน ใช้ flag + bit stuffing มี flow/error control ด้วย sequence number และ ACK ทำงานได้ทั้ง half และ full duplex |
| **NRM / ABM** | โหมดของ HDLC: Normal Response Mode (secondary ต้องรอ primary สั่งก่อนจึงส่งได้) · Asynchronous Balanced Mode (สองฝั่งเท่ากัน ส่งเองได้) |
| **I-frame / S-frame / U-frame** | Information (ข้อมูล+ACK piggyback) · Supervisory (คุม flow/error control อย่างเดียว) · Unnumbered (จัดการ session เช่น connect/disconnect) |
| **P/F bit** | Poll/Final primary ส่งเป็น Poll, secondary ตอบเป็น Final |
| **N(S) / N(R)** | เลข frame ที่ส่ง / เลข ACK ที่ piggyback ไปด้วย |
| **RR / RNR / REJ / SREJ** | S-frame: Receiver Ready (ACK ปกติ) · Receiver Not Ready (ACK แต่ช้าลงหน่อย) · Reject (NAK ของ Go-Back-N) · Selective Reject (NAK ของ Selective Repeat) |
| **Connectionless / Connection-oriented** | ไม่ต้อง/ต้องตั้ง connection ก่อนส่ง ส่วนแบบมี connection ติดตาม sequence number, ACK, flow state HDLC รองรับทั้งสอง |

---

## 📡 Lecture 6.1 — Media Access Control (MAC)

| ศัพท์ | คืออะไร |
|---|---|
| **Simplex** | ส่งทางเดียว เช่น ทีวี วิทยุ รีโมต |
| **Half-duplex** | ส่งหรือรับได้ทีละทิศบนสื่อที่แชร์ เช่น WLAN และ hub |
| **Full-duplex** | ส่งและรับพร้อมกันได้ เช่น Ethernet switch |
| **Physical / Logical topology** | การเชื่อมต่อจริงของอุปกรณ์ / การเชื่อมต่อเชิงตรรกะตาม interface และ IP |
| **Multiple access protocol** | กติกาควบคุมว่าใครส่งได้เมื่อไรบนช่องแชร์ เพื่อลดการชน |
| **Collision** | สถานีสองเครื่องขึ้นไปส่งพร้อมกัน สัญญาณเสียหาย |
| **Contention-based (Random access)** | แย่งกันส่งเอง ไม่มีตัวจัดคิว ง่าย เหมาะกับ traffic เบาถึงปานกลาง แต่แย่เมื่อโหลดหนัก เช่น ALOHA, CSMA |
| **Controlled access** | ต้องได้รับอนุญาตก่อนส่ง ทุกคนมีตาส่ง (Reservation, Polling, Token passing) |
| **Channelization** | แบ่งแบนด์วิดท์ของลิงก์ให้แต่ละสถานี (FDMA, TDMA, CDMA, OFDMA) |
| **ALOHA** | random access แรกสุด (ต้นทศวรรษ 1970) ใครมี frame ก็ส่งเลย ไม่ sense carrier ไม่ตรวจชน ส่งแล้วรอ ACK ถ้าไม่มาในเวลาที่กำหนด (2 เท่า max propagation delay) ส่งใหม่หลังรอเวลาสุ่ม |
| **Pure ALOHA / Slotted ALOHA** | Pure ส่งได้ทุกเมื่อ · Slotted แบ่งเวลาเป็น slot ส่งได้เฉพาะต้น slot ทำให้ vulnerable time สั้นลง (Pure = 2 เท่าของเวลาส่ง frame, Slotted = 1 เท่า) |
| **Vulnerable time** | ช่วงเวลาที่อาจเกิดการชน |
| **CSMA** | Carrier Sense Multiple Access ฟังสื่อก่อนส่ง ลดการชนแต่ไม่หมด เพราะ propagation delay ทำให้ช่องดูว่างทั้งที่มีคนเริ่มส่งแล้ว |
| **Persistence strategy** | พฤติกรรมเมื่อเจอช่องไม่ว่าง: Non-persistent (รอสุ่มแล้วฟังใหม่) · 1-persistent (ฟังต่อเนื่อง ว่างเมื่อไรส่งทันที) · p-persistent (ว่างแล้วส่งด้วยความน่าจะเป็น p) |
| **CSMA/CD** | เพิ่มการตรวจจับการชน (Collision Detection) ส่งไปด้วยฟังไปด้วย ถ้าชนก็หยุดแล้ว backoff แล้วส่งใหม่ ใช้ใน Ethernet แบบ bus/hub (half-duplex) |
| **Exponential backoff** | หลังชนรอเวลาสุ่มระหว่าง 0 ถึง (2^N − 1) x เวลา (N = จำนวนครั้งที่พยายาม) ยิ่งชนซ้ำยิ่งรอนาน |
| **CSMA/CA** | หลีกเลี่ยงการชน (Collision Avoidance) ไม่ตรวจชน ฟังช่อง รอ IFS แล้วรอ contention window สุ่ม แล้วส่ง รอ ACK ใช้ใน Wi-Fi (802.11) |
| **IFG / IFS** | Interframe gap/space ช่วงเวลารอหลังพบว่าช่องว่าง ค่ายิ่งสูง priority ยิ่งต่ำ |
| **Contention window** | ช่วงเวลาที่แบ่งเป็น slot สถานีสุ่มจำนวน slot ที่จะรอ ขนาดเพิ่มเป็นสองเท่าทุกครั้งที่ช่องไม่ว่าง (binary exponential backoff) และหยุดนับเมื่อช่องไม่ว่าง |
| **RTS / CTS** | Request to Send / Clear to Send ข้อความขอจองช่อง และอนุญาตให้ส่ง ใน CSMA/CA |
| **NAV** | Network Allocation Vector ตัวจับเวลาที่สถานีอื่นตั้งตามช่วงเวลาที่ RTS ขอจอง เพื่อไม่ฟังช่องจนกว่าจะหมดเวลา |
| **DCF / DIFS / SIFS** | Distributed Coordination Function (กลไก MAC ของ Wi-Fi) · DCF Interframe Spacing · Short Interframe Space (สั้นกว่า ใช้ตอบ ACK/CTS) |
| **Reservation** | มี reservation frame นำหน้า มี minislot ให้ N สถานี ใครจะส่งต้องจองช่องของตัวเอง แล้วส่งตามลำดับหลังช่วงจอง |
| **Polling** | มี primary (master) คอยถามแต่ละ secondary (slave) ทีละตัวว่ามีข้อมูลจะส่งไหม ทุกการสื่อสารผ่าน primary (select และ poll) |
| **Token passing** | สถานีเรียงเป็นวงแหวน ส่ง token วนไป ใครถือ token จึงส่งได้ (เช่น Token Ring) |
| **FDMA** | แบ่งตามความถี่ แต่ละสถานีได้ย่านของตัวเอง ใช้ในโทรศัพท์มือถือและดาวเทียม |
| **TDMA** | แบ่งตามเวลา แต่ละสถานีได้ time slot ของตัวเอง |
| **CDMA** | ทุกสถานีส่งพร้อมกันในความถี่เดียว แต่แยกกันด้วยรหัส (orthogonal code) |
| **OFDMA** | แบ่งเป็น subcarrier ย่อยที่ตั้งฉากกัน (orthogonal) แจกจ่ายให้หลายผู้ใช้ ใช้ใน 4G/5G และ Wi-Fi 6 |

---

## 🔌 Lecture 6.2 — Ethernet

| ศัพท์ | คืออะไร |
|---|---|
| **Ethernet / IEEE 802.3** | มาตรฐาน LAN ที่รวม data link และ physical layer ไว้ด้วยกัน เกิดที่ Xerox PARC (Metcalfe) แรงบันดาลใจจาก ALOHAnet กลายเป็น 802.3 ปี 1983 |
| **IEEE Project 802** | โครงการรวมมาตรฐาน LAN ของ physical และ data link layer |
| **Connectionless service** | Ethernet ส่ง frame แต่ละอันอิสระ ไม่ตั้ง/ไม่ปิด connection ไม่มี flow control (ปล่อยให้ TCP จัดการ) ไม่รู้ว่า frame ตก |
| **Preamble** | 7 ไบต์ 0/1 สลับกัน ใช้ซิงก์ clock ผู้รับ เพิ่มที่ physical layer |
| **SFD** | Start Frame Delimiter 1 ไบต์ 10101011 บอกจุดเริ่มต้น frame |
| **DA / SA** | Destination / Source Address ที่อยู่ปลายทาง/ต้นทาง ยาว 6 ไบต์ (48 บิต) |
| **Type field** | บอกว่าข้อมูลข้างในเป็น protocol ชั้นบนอะไร เช่น IP, ARP |
| **Data / Padding** | ข้อมูลขนาด 46 ถึง 1500 ไบต์ ถ้าสั้นไปต้องเติม 0 (padding) ให้ถึงขั้นต่ำ |
| **CRC-32 (FCS)** | ตรวจ error ท้าย frame ครอบคลุม address, type, data ถ้าผิดผู้รับทิ้ง frame เงียบๆ |
| **ขนาด frame** | ต่ำสุด 64 ไบต์ (512 บิต) เพื่อรองรับ CSMA/CD สูงสุด 1518 ไบต์ (header+trailer = 18 ไบต์ ดังนั้น payload 46–1500) |
| **MAC address** | ที่อยู่ link layer 48 บิต เขียนเป็น hex เช่น 4A:30:10:21:10:1A 24 บิตแรก = OUI ที่ IEEE กำหนดให้ผู้ผลิต 24 บิตหลังผู้ผลิตกำหนดเอง |
| **NIC** | Network Interface Card การ์ดเครือข่ายที่ให้ MAC address แก่สถานี |
| **Unicast / Multicast / Broadcast** | ส่งหาเครื่องเดียว / ส่งหากลุ่ม / ส่งหาทุกเครื่อง (FF:FF:FF:FF:FF:FF) multicast ใช้เป็นปลายทางเท่านั้น ต้นทางเป็น unicast เสมอ |
| **MAC vs IP ระหว่างทาง** | IP ต้นทาง/ปลายทางไม่เปลี่ยน แต่ MAC address เปลี่ยนทุก hop |
| **Default gateway** | router ที่ host ส่ง frame ไปหาเมื่อปลายทางอยู่นอก LAN (ใช้ MAC ของ gateway) |
| **Standard Ethernet** | 10 Mbps บน bus/hub ใช้ CSMA/CD แบบ 1-persistent frame ขั้นต่ำ 64 ไบต์เพราะต้องตรวจชนได้ทันก่อนส่งจบ สายยาวสุดราว 2500 เมตร |
| **Fast Ethernet** | 100 Mbps frame ขั้นต่ำยัง 64 ไบต์ แบบ hub สายยาวสุดลดเหลือ 250 เมตร (ใช้จริง 100 เมตร) แบบ switch ไม่ต้อง CSMA/CD |
| **Gigabit Ethernet** | 1 Gbps (IEEE 802.3z) ไม่มี hub ใช้ switch+full-duplex จึงไม่ชน มี Carrier Extension (ขยาย frame ขั้นต่ำเป็น 512 ไบต์) และ Frame Bursting (รวมหลาย frame เป็นก้อนใหญ่) |
| **Autonegotiation** | อุปกรณ์สองฝั่งต่อรองความเร็วและ duplex ที่ดีที่สุดเอง |
| **Auto-MDIX** | switch ตรวจชนิดสาย (straight-through หรือ crossover) เองแล้วปรับพอร์ต ไม่ใช่เรื่องเดียวกับ autonegotiation |
| **Collision domain** | ขอบเขตที่การส่งพร้อมกันจะชนกัน switch แยก collision domain ต่อ 1 พอร์ต |
| **Switch learning** | switch ดู source MAC ของ frame ที่เข้ามา แล้วจดลง MAC address table พร้อมเลขพอร์ต (เก็บราว 5 นาที) ถ้า MAC เดิมมาจากพอร์ตใหม่ อัปเดตเป็นพอร์ตใหม่ |
| **Filtering / Forwarding** | ถ้า destination MAC อยู่ในตาราง ส่งออกพอร์ตที่ตรงกันเท่านั้น |
| **Flooding / Unknown unicast** | ถ้า destination ไม่อยู่ในตาราง (unknown unicast) หรือเป็น broadcast/multicast ส่งออกทุกพอร์ตยกเว้นพอร์ตที่เข้ามา |
| **Store-and-forward switch** | รับ frame ครบ ตรวจ CRC แล้วจึงส่งต่อ จำเป็นสำหรับ QoS |
| **Cut-through switch** | เริ่มส่งต่อเมื่ออ่าน destination address ได้ ไม่ต้องรอครบ เร็วกว่า มี 2 แบบ: fast-forward (พื้นฐาน) และ fragment-free (ตรวจ 64 ไบต์แรกก่อน) |

---

## 🧭 Lecture 7 — ARP, Switch, STP, VLAN

| ศัพท์ | คืออะไร |
|---|---|
| **ARP** | Address Resolution Protocol แปลง IP address เป็น MAC address ใน LAN แบบ request-response ข้อความถูกห่อใน link layer frame โดยตรง |
| **ARP request / reply** | Request = broadcast ถามทุกเครื่อง (ช่อง MAC ปลายทางเป็น 0 ทั้งหมด) · Reply = เครื่องเจ้าของ IP ตอบกลับตรงถึงผู้ถาม |
| **ARP cache** | ตารางจับคู่ IP กับ MAC ที่ OS เก็บไว้ Dynamic (ARP สร้างเอง หมดอายุ) หรือ Static (ตั้งเองถาวร) ดูได้ด้วย `arp -a` |
| **Repeater** | อุปกรณ์ physical layer ที่สร้างสัญญาณใหม่ (regenerate) ไม่ใช่ขยาย ช่วยต่อสายให้ไกลขึ้น |
| **Hub** | repeater หลายพอร์ต ส่ง frame ออกทุกพอร์ตยกเว้นพอร์ตที่เข้ามา ไม่มี MAC address ไม่กรอง ไม่ฉลาด |
| **Bridge** | อุปกรณ์ data link layer มี 2 พอร์ต มีตารางเพื่อกรอง (filtering) ไม่แก้ MAC ใน frame |
| **Switch** | bridge หลายพอร์ตที่เรียนรู้เองได้ (self-learning) แยก collision domain ทีละพอร์ต ทำงานทั้ง physical และ data link |
| **Transparent switch** | switch ที่เครื่องในเครือข่ายไม่รู้ว่ามีอยู่ (IEEE 802.1d) ต้อง: ส่งต่อ frame ได้, อัปเดตตารางเองจากการเรียนรู้, และป้องกัน loop |
| **Loop problem** | มี switch สำรองหลายตัว ทำให้เกิดเส้นทางวนลูป frame ซ้ำเพิ่มไม่หยุด เพราะ Ethernet frame ไม่มี TTL |
| **STP** | Spanning Tree Protocol (IEEE 802.1d) ให้ switch คุยกันแล้วสร้างโครงสร้างต้นไม้ไม่มี loop ด้วยการบล็อกลิงก์สำรอง |
| **Root switch (Root bridge)** | switch ที่มี ID ต่ำสุด ถูกเลือกเป็นรากของต้นไม้ |
| **Cost / Shortest path** | ค่าใช้จ่ายของแต่ละลิงก์ (ในสไลด์ใช้ hop count) หาเส้นทางต้นทุนต่ำสุดจาก root ไปทุกโหนด (ใช้ Dijkstra) |
| **Forwarding port / Blocking port** | พอร์ตที่อยู่ในต้นไม้ ส่งต่อ frame ปกติ / พอร์ตนอกต้นไม้ บล็อก frame เพื่อกัน loop แต่เก็บลิงก์ไว้เป็นเส้นทางสำรอง |
| **VLAN** | Virtual LAN แบ่งกลุ่มอุปกรณ์เชิงตรรกะบน switch ตัวเดียวหรือหลายตัว 1 VLAN = 1 broadcast domain = ปกติ 1 IP subnet |
| **Broadcast domain** | ขอบเขตที่ broadcast ไปถึง VLAN แบ่งให้เล็กลง ลด traffic |
| **Benefits ของ VLAN** | broadcast domain เล็กลง, ปลอดภัยขึ้น (คุยได้เฉพาะ VLAN เดียวกัน), จัดการง่าย, ประหยัด (switch ตัวเดียวรองรับหลายกลุ่ม), performance ดีขึ้น |
| **Access port** | พอร์ตที่ต่ออุปกรณ์ปลายทาง อยู่ใน data VLAN เดียว frame ออกจากพอร์ตไม่มี 802.1Q tag (ใน Netgear เรียก Untagged) |
| **Trunk** | ลิงก์จุดต่อจุดระหว่างอุปกรณ์ ที่ส่ง traffic ของหลาย VLAN พร้อมกัน ใช้ tagging 802.1Q (ใน Netgear เรียก Tagged) |
| **IEEE 802.1Q tag** | tag ยาว 4 ไบต์ใน frame: TPID 0x8100 (2 ไบต์), User priority (3 บิต), CFI (1 บิต), VLAN ID (12 บิต รองรับ 4096 VLAN) ใส่แล้วต้องคำนวณ FCS ใหม่ และดึง tag ออกก่อนส่งถึงเครื่องปลายทาง |
| **Default VLAN** | VLAN 1 เป็นทั้ง default, native และ management VLAN ลบหรือเปลี่ยนชื่อไม่ได้ |
| **Native VLAN** | ใช้กับ trunk เท่านั้น frame ของ native VLAN จะไม่ถูกติด tag บน trunk |
| **Data VLAN** | VLAN สำหรับ traffic ของผู้ใช้ เช่น เว็บและอีเมล |
| **Management VLAN** | VLAN สำหรับจัดการอุปกรณ์ (SSH/Telnet) ปกติคือ SVI ของ switch ไม่ควรปนกับ traffic ผู้ใช้ |
| **Voice VLAN** | VLAN แยกสำหรับ IP phone โทรศัพท์ติด tag traffic เสียงเอง พร้อมค่า CoS (QoS ระดับ layer 2) switch แจ้ง voice VLAN ผ่าน CDP |
| **SVI** | Switched Virtual Interface อินเทอร์เฟซเสมือนของ VLAN บน switch ใช้ให้ switch มี IP เพื่อจัดการ |
| **Normal / Extended range VLAN** | Normal = VLAN 1–1005 (เก็บใน vlan.dat) · Extended = 1006–4095 (ผู้ให้บริการใช้ เก็บใน running-config) |
| **VTP** | VLAN Trunking Protocol ซิงก์ข้อมูล VLAN ระหว่าง switch (normal range) |
| **Inter-VLAN routing** | VLAN ต่างกันคุยกันต้องผ่านอุปกรณ์ layer 3 (router หรือ layer 3 switch) ที่เป็น gateway ของแต่ละ VLAN |
| **PVID** | Port VLAN ID VLAN ที่ frame ไม่มี tag ที่เข้าพอร์ตนั้นจะถูกจัดเข้า (ตั้งให้ตรงกับ VLAN ของพอร์ต) |
| **คำสั่ง VLAN ที่ควรรู้** | `vlan [id]` + `name` สร้าง VLAN · `switchport mode access` + `switchport access vlan [id]` กำหนดพอร์ต · `switchport mode trunk` + `switchport trunk native vlan` / `allowed vlan` ตั้ง trunk · `show vlan brief` ตรวจสอบ · `no vlan [id]` ลบ |

> ⚠️ EtherChannel (ตาม syllabus สัปดาห์ 8) ไม่มีอยู่ในสไลด์ Lecture 7 ที่มี จึงยังไม่ได้ใส่ในคลังนี้ ถ้ามีสไลด์ส่งมาเพิ่ม จะเติมให้

---

# Quiz คำศัพท์

| ศัพท์ | คืออะไร |
|---|---|
| **Parity Check** | เติม parity bit 1 บิตท้ายข้อมูลให้จำนวนบิต 1 เป็นคู่ (even parity) หรือคี่ (odd parity) จับ error จำนวนคี่บิตได้ แต่ error จำนวนคู่บิตจับไม่ได้ |
| **Checksum** | แบ่งข้อมูลเป็นชุด m บิต บวกกันแบบ one's complement แล้ว complement ผลรวมส่งไปด้วย ผู้รับบวกทุกชุดรวมกับ checksum ได้ 0 = ปกติ (ใช้ใน IPv4, TCP, UDP) |
| **CRC** | Cyclic Redundancy Check หารข้อมูลด้วย divisor แบบ modulo-2 (XOR) เอาเศษต่อท้ายเป็น FCS จับ burst error ได้ดีที่สุด ใช้เป็น FCS ของ Ethernet |
| **Syndrome** | ค่าที่ผู้รับคำนวณจาก codeword ที่ได้รับ = 0 แปลว่าไม่มี error ไม่ใช่ 0 แปลว่ามี error (ใน Hamming code ค่านี้บอกตำแหน่งบิตที่ผิด) |
| **Framing** | การแบ่งสตรีมบิตเป็น frame โดยกำหนดจุดเริ่ม–จุดจบ เพื่อให้ผู้รับแยกแต่ละ frame ออก เช่น ใช้ flag + stuffing หรือฟิลด์ความยาว |
| **Flow Control** | คุมอัตราส่งของ sender ไม่ให้เร็วเกินจน receiver รับไม่ทันหรือ buffer ล้น (เช่น Stop-and-Wait, Sliding Window) |
| **Error Control** | กลไกจัดการเมื่อ frame หายหรือเสีย โดยใช้ ACK + timeout + retransmission (คำตอบข้อ 1 ของโจทย์ในไฟล์) |
| **ACK** | Acknowledgment ข้อความที่ receiver ตอบกลับ ยืนยันว่ารับ frame ถูกต้อง ใน tutorial นี้ใช้ positive ACK เท่านั้น (Go-Back-N: ACK k = ได้รับครบถึง k−1 และรอ frame k) |
| **Stop-and-Wait ARQ** | ส่งทีละ 1 frame แล้วรอ ACK ก่อนส่ง frame ถัดไป ใช้เลข 0 กับ 1 สลับกัน ง่ายแต่ช้า ใช้ลิงก์ไม่คุ้ม |
| **Go-Back-N ARQ** | ส่งแบบ pipeline ได้ sender window ≤ 2^m − 1 แต่ receiver window = 1 frame ที่มาผิดลำดับจะถูกทิ้ง ถ้า timeout ส่งซ้ำตั้งแต่ frame ที่หายไปจนถึง frame ล่าสุดที่ส่ง |
| **Selective Repeat ARQ** | receiver เก็บ frame ที่มาผิดลำดับไว้ใน buffer ได้ และส่งซ้ำเฉพาะ frame ที่หายหรือเสีย window ทั้งสองฝั่ง ≤ 2^(m−1) ใช้ individual ACK |
| **Sliding Window** | หน้าต่างที่กำหนดว่าส่ง frame ค้างไว้ได้กี่ตัวโดยยังไม่ได้ ACK เมื่อได้ ACK หน้าต่างจะเลื่อนไปข้างหน้า |
| **Pipelining** | ส่งหลาย frame ต่อเนื่องโดยไม่ต้องรอ ACK ทีละตัว (Go-Back-N และ Selective Repeat ใช้ ส่วน Stop-and-Wait ไม่ใช้) |
| **CSMA/CD** | Carrier Sense Multiple Access with Collision Detection ฟังสื่อก่อนส่ง ส่งไปด้วยฟังไปด้วย ถ้าตรวจพบการชนก็หยุด แล้วรอ random backoff ก่อนส่งใหม่ ใช้ใน Ethernet แบบ bus/hub |
| **CSMA/CA** | Carrier Sense Multiple Access with Collision Avoidance ฟังสื่อก่อนส่งและใช้ random backoff เพื่อหลีกเลี่ยงการชน (ไม่ตรวจชน) รอ ACK หลังส่ง ใช้ใน WLAN / Wi-Fi |
| **ALOHA** | random access แบบแรกสุด มี frame ก็ส่งทันทีโดยไม่ฟังสื่อ ไม่ตรวจชน ถ้าไม่ได้ ACK ในเวลาที่กำหนดก็รอเวลาสุ่มแล้วส่งใหม่ (มี Pure และ Slotted) |
| **Polling** | controlled access แบบมีอุปกรณ์กลาง (primary) เรียกถามแต่ละ station ตามลำดับว่ามีข้อมูลจะส่งไหม |
| **Token Passing** | controlled access ที่สิทธิ์ในการส่งถูกส่งต่อกันด้วย control frame พิเศษที่เรียกว่า token ใครถือ token ถึงส่งได้ (เช่น Token Ring) |
| **Reservation** | controlled access ที่แต่ละ station ต้องจองช่วงเวลาส่งล่วงหน้าใน reservation frame ก่อน แล้วจึงส่งตามลำดับที่จอง |
| **FDMA** | Frequency Division Multiple Access channelization แบบแบ่งย่านความถี่ ให้แต่ละ station ได้ย่านของตัวเอง |
| **TDMA** | Time Division Multiple Access channelization แบบแบ่งเวลา ให้แต่ละ station ได้ time slot ของตัวเอง |
| **CDMA** | Code Division Multiple Access ทุก station ส่งพร้อมกันในช่วงเวลาและย่านความถี่เดียวกัน โดย receiver แยกผู้ใช้ด้วย orthogonal code (คำตอบข้อ 7) |
| **OFDMA** | Orthogonal Frequency Division Multiple Access แบ่งย่านความถี่เป็น subcarrier ย่อยที่ตั้งฉากกัน แล้วแจกจ่ายให้หลายผู้ใช้ ใช้ใน 4G/5G และ Wi-Fi 6 |
| **Collision** | สอง station ขึ้นไปส่งบนสื่อแชร์เดียวกันพร้อมกัน สัญญาณชนกันจนข้อมูลเสียหาย ต้องส่งใหม่ |
| **Two-Dimensional (2D) Even Parity** | ตรวจ even parity ทั้งแนวนอน (ต่อแถว) และแนวตั้ง (ต่อหลัก) ถ้ามี d datawords ยาว k บิต จะได้ block ขนาด (d+1)(k+1) บิต เช่น 3 แถว x 4 บิต = (3+1)(4+1) = 20 บิต (ข้อ 5) |
| **Dataword / Codeword** | Dataword = ข้อมูลเดิม k บิต · Codeword = ข้อมูลรวมบิต redundancy ที่เติม n = k + r บิต |
| **Sequence number (m bits) / Modulo** | เลขกำกับ frame ใช้ m บิตได้เลข 0 ถึง 2^m − 1 แล้ววนกลับ (modulo 2^m) เช่น m = 3 คือ modulo 8 เลข 0–7 |
| **Sender window / Receiver window** | จำนวน frame สูงสุดที่ sender ส่งค้างได้ / ที่ receiver ยอมรับได้ Go-Back-N: sender ≤ 2^m − 1, receiver = 1 · Selective Repeat: ทั้งสองฝั่ง ≤ 2^(m−1) (m = 4 ได้ 8 ทั้งคู่ ข้อ 6) |
| **Sf / Sn / R** | Sf = frame แรกสุดที่ส่งแล้วยังไม่ได้ ACK · Sn = เลข frame ถัดไปที่จะส่ง · R = เลข frame ที่ receiver กำลังรอรับ |
| **Timer / Timeout** | sender จับเวลารอ ACK ถ้าหมดเวลาโดยไม่ได้ ACK ถือว่า frame หายหรือเสีย ต้องส่งซ้ำ |
| **Retransmission** | การส่ง frame เดิมซ้ำเมื่อ timeout หรือได้ NAK Go-Back-N ส่งซ้ำ frame ที่หายและทุก frame หลังมัน (ข้อ 9: ส่ง 5, 6, 7) · Selective Repeat ส่งซ้ำเฉพาะตัวที่หาย |
| **Positive cumulative ACK** | ACK แบบสะสมของ Go-Back-N ACK k แปลว่าได้รับ frame ถึง k−1 ครบตามลำดับและกำลังรอ frame k |
| **Positive individual ACK** | ACK ทีละ frame ของ Selective Repeat ACK k แปลว่าได้รับ frame k ถูกต้องแล้ว (ไม่ว่าจะมาตามลำดับหรือไม่) |
| **Duplicate ACK** | ACK ซ้ำเลขเดิม ใน Go-Back-N เมื่อ frame มาผิดลำดับ receiver จะส่ง cumulative ACK ล่าสุดซ้ำ (ข้อ 9: ACK 5, 5, 5) |
| **NAK** | Negative Acknowledgment ข้อความแจ้งว่า frame ที่คาดหวังยังไม่มา/เสีย ให้ sender ส่งใหม่ทันทีโดยไม่ต้องรอ timer (ข้อ 10 ใช้ NAK 5) |
| **Buffer** | ที่พักข้อมูลชั่วคราว sender เก็บสำเนา frame ที่ยังไม่ได้ ACK ส่วน receiver ของ Selective Repeat เก็บ frame ที่มาผิดลำดับไว้รอตัวที่ขาด |
| **Out-of-order frame** | frame ที่มาถึงผิดลำดับ (ข้ามเลขที่รออยู่) Go-Back-N ทิ้ง · Selective Repeat เก็บ buffer ไว้และตอบ ACK ของ frame นั้น |
| **Orthogonal code** | รหัสที่ตั้งฉากกัน (ผลคูณภายในเป็น 0) ใช้ใน CDMA ให้ผู้ใช้หลายคนส่งพร้อมกันได้แล้ว receiver แยกสัญญาณของแต่ละคนออกได้ |
| **Random backoff** | การรอเวลาแบบสุ่มก่อนลองส่งใหม่ เพื่อไม่ให้หลาย station กลับมาส่งพร้อมกันอีก ใช้ใน CSMA/CD, CSMA/CA และ ALOHA |
| **Controlled access** | ต้องได้รับอนุญาตก่อนส่ง ทุก station มีตาส่ง ไม่แย่งกัน เช่น Polling, Token Passing, Reservation (ต่างจาก random access เช่น ALOHA, CSMA) |
| **Multiple access / MAC protocol** | กติกาที่กำหนดว่า station ไหนส่งได้เมื่อไรบนสื่อ (medium) ที่หลายเครื่องแชร์กัน เพื่อลด collision แบ่งเป็น random access, controlled access, channelization |
| **Medium** | สื่อ/ช่องสัญญาณที่ใช้ส่งข้อมูล เช่น สายทองแดง ใยแก้ว หรืออากาศ (ไร้สาย) |
| **Frame** | หน่วยข้อมูลของ Data Link Layer ประกอบด้วย header, payload และ trailer |
